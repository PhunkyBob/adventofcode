"""
Step-by-step visualization of Day 3 2025

Usage: uv run day_03_viz.py
"""

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget

# Font for emoji support
EMOJI_FONT = "seguiemj"

# Emojis for conditions
CHECK_YES = "✅"  # Green check for true condition
CHECK_NO = "❌"  # Red cross for false condition

# Configuration
INPUT_STRING = "234234234234278"
NB_DIGITS = 12

# Colors (RGBA)
COLOR_DEFAULT = (0.3, 0.3, 0.4, 1)  # Dark gray - unprocessed element
COLOR_PROCESSED = (0.1, 0.1, 0.1, 1)  # Very dark gray - already processed
COLOR_CURRENT = (0.2, 0.6, 0.9, 1)  # Blue - current element
COLOR_STACK = (0.2, 0.8, 0.6, 0.7)  # Cyan - in stack
COLOR_STACK_TOP = (0.9, 0.7, 0.2, 1)  # Orange - top of stack (compared)
COLOR_POPPING = (0.9, 0.3, 0.3, 1)  # Red - being popped
COLOR_PUSHING = (0.3, 1, 0.4, 1)  # Green - being pushed
COLOR_BG = (0.12, 0.12, 0.15, 1)  # Background
COLOR_TEXT = (0.9, 0.9, 0.95, 1)  # Text color
COLOR_BUTTON_BG = (0.3, 0.3, 0.35, 1)  # Button background

FONT_SIZE_LARGE = dp(32)
FONT_SIZE_MEDIUM = dp(24)
FONT_SIZE_SMALL = dp(14)


class StepType(Enum):
    START = "start"
    NEW_DIGIT = "new_digit"
    CHECK_WHILE = "check_while"
    POP = "pop"
    EXIT_WHILE = "exit_while"
    CHECK_PUSH = "check_push"
    PUSH = "push"
    AFTER_PUSH = "after_push"
    SKIP_PUSH = "skip_push"
    END = "end"


@dataclass
class Step:
    """Represents a step of the algorithm."""

    step_type: StepType
    i: int  # Index in input
    digit: int  # Current digit
    stack: List[int]  # Stack state
    description: str  # Action description
    condition_info: Optional[str] = None  # Condition info
    highlight_top: bool = False  # Highlight top of stack
    is_popping: bool = False  # Pop animation
    is_pushing: bool = False  # Push animation


def generate_steps(line: List[int], nb_digits: int) -> List[Step]:
    """Generate all algorithm steps."""
    steps: List[Step] = []
    stack: List[int] = []
    n = len(line)

    steps.append(
        Step(
            step_type=StepType.START,
            i=-1,
            digit=-1,
            stack=stack.copy(),
            description=f"Start: input={line}, nb_digits={nb_digits}, n={n}",
        )
    )

    for i, digit in enumerate(line):
        # Start of iteration
        steps.append(
            Step(
                step_type=StepType.NEW_DIGIT,
                i=i,
                digit=digit,
                stack=stack.copy(),
                description=f"New digit: digit={digit} (position {i})",
            )
        )

        # While loop
        while stack and stack[-1] < digit and len(stack) + (n - i) > nb_digits:
            top = stack[-1]
            remaining = n - i
            condition_info = (
                f"While conditions:\n"
                f"  {CHECK_YES} stack not empty? YES (stack={stack})\n"
                f"  {CHECK_YES if top < digit else CHECK_NO} stack[-1]={top} < digit={digit}? {'YES' if top < digit else 'NO'}\n"
                f"  {CHECK_YES if len(stack) + remaining > nb_digits else CHECK_NO} len(stack)={len(stack)} + remaining={remaining} = {len(stack) + remaining} > {nb_digits}? "
                f"{'YES' if len(stack) + remaining > nb_digits else 'NO'}\n"
                f"→ All conditions TRUE → Pop!"
            )
            steps.append(
                Step(
                    step_type=StepType.CHECK_WHILE,
                    i=i,
                    digit=digit,
                    stack=stack.copy(),
                    description=f"Checking while: {top} < {digit} and enough room",
                    condition_info=condition_info,
                    highlight_top=True,
                )
            )

            steps.append(
                Step(
                    step_type=StepType.POP,
                    i=i,
                    digit=digit,
                    stack=stack.copy(),
                    description=f"POP: removing {top} from stack",
                    is_popping=True,
                    highlight_top=True,
                )
            )
            stack.pop()

        # Show why while loop exits
        if stack:
            top = stack[-1]
            remaining = n - i
            cond1 = stack[-1] < digit
            cond2 = len(stack) + remaining > nb_digits
            if not cond1 or not cond2:
                reason = []
                if not cond1:
                    reason.append(f"stack[-1]={top} >= digit={digit}")
                if not cond2:
                    reason.append(
                        f"len(stack)={len(stack)} + remaining={remaining} = {len(stack) + remaining} <= {nb_digits}"
                    )
                condition_info = (
                    f"While conditions:\n"
                    f"  {CHECK_YES} stack not empty? YES\n"
                    f"  {CHECK_YES if cond1 else CHECK_NO} stack[-1]={top} < digit={digit}? {'YES' if cond1 else 'NO'}\n"
                    f"  {CHECK_YES if cond2 else CHECK_NO} len(stack)={len(stack)} + remaining={remaining} > {nb_digits}? {'YES' if cond2 else 'NO'}\n"
                    f"→ Condition(s) FALSE → Exit while"
                )
                steps.append(
                    Step(
                        step_type=StepType.EXIT_WHILE,
                        i=i,
                        digit=digit,
                        stack=stack.copy(),
                        description=f"Exiting while: {', '.join(reason)}",
                        condition_info=condition_info,
                        highlight_top=True,
                    )
                )
        elif not stack:
            steps.append(
                Step(
                    step_type=StepType.EXIT_WHILE,
                    i=i,
                    digit=digit,
                    stack=stack.copy(),
                    description="Exiting while: stack empty",
                    condition_info=f"While conditions:\n  {CHECK_NO} stack not empty? NO\n→ Exit while",
                )
            )

        # Check push
        if len(stack) < nb_digits:
            condition_info = (
                f"Push condition:\n"
                f"  {CHECK_YES} len(stack)={len(stack)} < nb_digits={nb_digits}? YES\n"
                f"→ Can add digit {digit}"
            )
            steps.append(
                Step(
                    step_type=StepType.CHECK_PUSH,
                    i=i,
                    digit=digit,
                    stack=stack.copy(),
                    description=f"Checking push: len(stack)={len(stack)} < {nb_digits}",
                    condition_info=condition_info,
                )
            )

            steps.append(
                Step(
                    step_type=StepType.PUSH,
                    i=i,
                    digit=digit,
                    stack=stack.copy(),
                    description=f"PUSH: adding {digit} to stack",
                    is_pushing=True,
                )
            )
            stack.append(digit)

            steps.append(
                Step(
                    step_type=StepType.AFTER_PUSH,
                    i=i,
                    digit=digit,
                    stack=stack.copy(),
                    description=f"Stack after push: {stack}",
                )
            )
        else:
            condition_info = (
                f"Push condition:\n"
                f"  {CHECK_NO} len(stack)={len(stack)} < nb_digits={nb_digits}? NO\n"
                f"→ Stack full, skipping {digit}"
            )
            steps.append(
                Step(
                    step_type=StepType.SKIP_PUSH,
                    i=i,
                    digit=digit,
                    stack=stack.copy(),
                    description=f"Stack full ({len(stack)}/{nb_digits}), skipping {digit}",
                    condition_info=condition_info,
                )
            )

    # End
    result = int("".join(map(str, stack)))
    steps.append(
        Step(
            step_type=StepType.END,
            i=len(line),
            digit=-1,
            stack=stack.copy(),
            description=f"DONE! Result: {''.join(map(str, stack))}",
        )
    )

    return steps


class DigitBox(Widget):
    """Widget representing a digit (in input or stack)."""

    def __init__(self, digit: str, size_hint=(None, None), size=(50, 50), **kwargs):
        super().__init__(size_hint=size_hint, size=size, **kwargs)
        self.digit = digit
        self.box_color = COLOR_DEFAULT
        self.text_color = COLOR_TEXT
        self.bind(pos=self.update_canvas, size=self.update_canvas)  # type: ignore[attr-defined]
        self.update_canvas()

    def set_color(self, color):
        self.box_color = color
        self.update_canvas()

    def update_canvas(self, *args):
        self.canvas.clear()  # type: ignore[union-attr]
        with self.canvas:  # type: ignore[attr-defined]
            Color(*self.box_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[8])

        # Remove old label if exists
        self.clear_widgets()
        label = Label(
            text=str(self.digit),
            font_size=FONT_SIZE_MEDIUM,
            bold=True,
            color=self.text_color,
            size=self.size,
            pos=self.pos,
            halign="center",
            valign="center",
        )
        label.text_size = label.size
        self.add_widget(label)


class InputArrayWidget(BoxLayout):
    """Widget displaying the input array."""

    def __init__(self, digits: List[int], **kwargs):
        super().__init__(orientation="horizontal", spacing=5, padding=10, size_hint=(None, None), **kwargs)
        self.digits = digits
        self.boxes: List[DigitBox] = []
        self.width = len(digits) * 55 + 20
        self.height = 70

        for d in digits:
            box = DigitBox(str(d), size=(50, 50))
            self.boxes.append(box)
            self.add_widget(box)

    def update_state(self, current_idx: int, processed_indices: set):
        """Update colors based on state."""
        for i, box in enumerate(self.boxes):
            if i < current_idx:
                box.set_color(COLOR_PROCESSED)
            elif i == current_idx:
                box.set_color(COLOR_CURRENT)
            else:
                box.set_color(COLOR_DEFAULT)


class StackWidget(BoxLayout):
    """Widget displaying the stack."""

    def __init__(self, max_size: int = 12, **kwargs):
        super().__init__(orientation="horizontal", spacing=5, padding=10, size_hint=(None, None), **kwargs)
        self.max_size = max_size
        self.boxes: List[DigitBox] = []
        self.width = max_size * 55 + 20
        self.height = 70

    def update_stack(
        self,
        stack: List[int],
        highlight_top: bool = False,
        is_popping: bool = False,
        is_pushing: bool = False,
        pushing_digit: Optional[int] = None,
    ):
        """Update stack display."""
        self.clear_widgets()
        self.boxes.clear()

        for i, d in enumerate(stack):
            box = DigitBox(str(d), size=(50, 50))
            is_top = i == len(stack) - 1

            if is_top and is_popping:
                box.set_color(COLOR_POPPING)
            elif is_top and highlight_top:
                box.set_color(COLOR_STACK_TOP)
            else:
                box.set_color(COLOR_STACK)

            self.boxes.append(box)
            self.add_widget(box)

        # Show digit being pushed
        if is_pushing and pushing_digit is not None:
            box = DigitBox(str(pushing_digit), size=(50, 50))
            box.set_color(COLOR_PUSHING)
            self.boxes.append(box)
            self.add_widget(box)

        # Placeholder for empty slots
        empty_slots = self.max_size - len(self.boxes)
        for _ in range(empty_slots):
            box = DigitBox("", size=(50, 50))
            box.set_color((0.15, 0.15, 0.18, 1))
            self.add_widget(box)


class VisualizerWidget(BoxLayout):
    """Main visualization widget."""

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=dp(15), padding=dp(20), **kwargs)

        # Generate steps
        self.input_digits = [int(c) for c in INPUT_STRING]
        self.steps = generate_steps(self.input_digits, NB_DIGITS)
        self.current_step = 0
        self.is_playing = False
        self.play_event = None

        # Title
        self.title_label = Label(
            text="🎄 Advent of Code 2025 - Day 3",
            font_name=EMOJI_FONT,
            font_size=FONT_SIZE_LARGE,
            bold=True,
            size_hint=(1, None),
            height=dp(50),
            color=COLOR_TEXT,
            halign="center",
            valign="middle",
        )
        self.title_label.bind(size=self._update_text_size)  # type: ignore[attr-defined]
        self.add_widget(self.title_label)

        # # Input info
        # self.input_info = Label(
        #     text=f'📥 Input: "{INPUT_STRING}" | Number of digits: {NB_DIGITS}',
        #     font_name=EMOJI_FONT,
        #     font_size=FONT_SIZE_MEDIUM,
        #     size_hint=(1, None),
        #     height=dp(30),
        #     color=COLOR_TEXT,
        #     halign="center",
        #     valign="middle",
        # )
        # self.input_info.bind(size=self._update_text_size)  # type: ignore[attr-defined]
        # self.add_widget(self.input_info)

        # Section: Input array
        input_section = BoxLayout(orientation="vertical", size_hint=(1, None), height=dp(100))
        input_label = Label(
            text="📋 Input array:",
            font_name=EMOJI_FONT,
            font_size=FONT_SIZE_MEDIUM,
            size_hint=(1, None),
            height=dp(25),
            halign="left",
            valign="middle",
            color=COLOR_TEXT,
        )
        input_label.bind(size=self._update_text_size)  # type: ignore[attr-defined]
        input_section.add_widget(input_label)

        input_container = BoxLayout(size_hint=(1, None), height=dp(75))
        self.input_widget = InputArrayWidget(self.input_digits)
        input_container.add_widget(self.input_widget)
        input_container.add_widget(Widget())  # Spacer
        input_section.add_widget(input_container)
        self.add_widget(input_section)

        # Section: Stack
        stack_section = BoxLayout(orientation="vertical", size_hint=(1, None), height=dp(100))
        stack_label = Label(
            text=f"📚 Stack ({NB_DIGITS}):",
            font_name=EMOJI_FONT,
            font_size=FONT_SIZE_MEDIUM,
            size_hint=(1, None),
            height=dp(25),
            halign="left",
            valign="middle",
            color=COLOR_TEXT,
        )
        stack_label.bind(size=self._update_text_size)  # type: ignore[attr-defined]
        stack_section.add_widget(stack_label)

        stack_container = BoxLayout(size_hint=(1, None), height=dp(75))
        self.stack_widget = StackWidget(max_size=NB_DIGITS)
        stack_container.add_widget(self.stack_widget)
        stack_container.add_widget(Widget())  # Spacer
        stack_section.add_widget(stack_container)
        self.add_widget(stack_section)

        # Section: Step description
        self.step_label = Label(
            text="",
            font_name=EMOJI_FONT,
            font_size=FONT_SIZE_MEDIUM,
            bold=True,
            size_hint=(1, None),
            height=dp(40),
            color=COLOR_TEXT,
            halign="center",
            valign="middle",
        )
        self.step_label.bind(size=self._update_text_size)  # type: ignore[attr-defined]
        self.add_widget(self.step_label)

        # Section: Conditions
        self.condition_label = Label(
            text="",
            font_name=EMOJI_FONT,
            font_size=FONT_SIZE_SMALL,
            size_hint=(1, None),
            height=dp(120),
            halign="left",
            valign="top",
            color=COLOR_TEXT,
        )
        self.condition_label.bind(size=self._update_text_size)  # type: ignore[attr-defined]
        self.add_widget(self.condition_label)

        # Color legend
        legend = self._create_legend()
        self.add_widget(legend)

        # Spacer
        self.add_widget(Widget(size_hint=(1, 1)))

        # Controls
        controls = self._create_controls()
        self.add_widget(controls)

        # Show first step
        self.update_display()

    def _update_text_size(self, instance, value):
        instance.text_size = (instance.width - 20, instance.height)

    def _create_legend(self) -> BoxLayout:
        """Create color legend."""
        legend = BoxLayout(orientation="horizontal", size_hint=(1, None), height=dp(40), spacing=dp(20))

        colors_info = [
            (COLOR_CURRENT, "Current"),
            (COLOR_PROCESSED, "Processed"),
            (COLOR_STACK, "In stack"),
            (COLOR_STACK_TOP, "Top element"),
            (COLOR_POPPING, "Pop"),
            (COLOR_PUSHING, "Push"),
        ]

        for color, text in colors_info:
            item = BoxLayout(orientation="horizontal", size_hint=(None, 1), width=dp(110), spacing=dp(5))

            color_box = Widget(size_hint=(None, None), size=(dp(20), dp(20)), pos_hint={"center_y": 0.5})
            with color_box.canvas:  # type: ignore[attr-defined]
                Color(*color)
                Rectangle(pos=color_box.pos, size=color_box.size)
            # Update the rectangle when the color box moves or resizes so it's kept centered
            color_box.bind(  # type: ignore[attr-defined]
                pos=lambda inst, val, c=color: self._update_legend_box(inst, c),
                size=lambda inst, val, c=color: self._update_legend_box(inst, c),
            )

            label = Label(
                text=text,
                font_size=FONT_SIZE_SMALL,
                color=COLOR_TEXT,
                halign="left",
                valign="middle",
            )
            label.bind(size=self._update_text_size)  # type: ignore[attr-defined]

            item.add_widget(color_box)
            item.add_widget(label)
            legend.add_widget(item)

        legend.add_widget(Widget())  # Spacer
        return legend

    def _update_legend_box(self, instance, color):
        instance.canvas.clear()
        with instance.canvas:
            Color(*color)
            Rectangle(pos=instance.pos, size=instance.size)

    def _create_controls(self) -> BoxLayout:
        """Create navigation controls."""
        controls = BoxLayout(orientation="vertical", size_hint=(1, None), height=dp(140), spacing=dp(10))

        # Buttons
        buttons = BoxLayout(orientation="horizontal", size_hint=(1, None), height=dp(50), spacing=dp(10))

        self.prev_btn = Button(
            text="⏮️ Previous",
            font_name=EMOJI_FONT,
            font_size=FONT_SIZE_SMALL,
            background_color=COLOR_BUTTON_BG,
            color=COLOR_TEXT,
        )
        self.prev_btn.bind(on_press=self.prev_step)  # type: ignore[attr-defined]

        self.play_btn = Button(
            text="▶️ Play",
            font_name=EMOJI_FONT,
            font_size=FONT_SIZE_SMALL,
            background_color=COLOR_BUTTON_BG,
            color=COLOR_TEXT,
        )
        self.play_btn.bind(on_press=self.toggle_play)  # type: ignore[attr-defined]

        self.next_btn = Button(
            text="Next ⏭️",
            font_name=EMOJI_FONT,
            font_size=FONT_SIZE_SMALL,
            background_color=COLOR_BUTTON_BG,
            color=COLOR_TEXT,
        )
        self.next_btn.bind(on_press=self.next_step)  # type: ignore[attr-defined]

        self.reset_btn = Button(
            text="🔄 Reset",
            font_name=EMOJI_FONT,
            font_size=FONT_SIZE_SMALL,
            background_color=COLOR_BUTTON_BG,
            color=COLOR_TEXT,
        )
        self.reset_btn.bind(on_press=self.reset)  # type: ignore[attr-defined]

        buttons.add_widget(self.prev_btn)
        buttons.add_widget(self.play_btn)
        buttons.add_widget(self.next_btn)
        buttons.add_widget(self.reset_btn)
        controls.add_widget(buttons)

        # Speed slider
        speed_layout = BoxLayout(orientation="horizontal", size_hint=(1, None), height=dp(50), spacing=dp(10))

        speed_lbl = Label(
            text="⏱️ Speed:",
            font_name=EMOJI_FONT,
            size_hint=(None, 1),
            width=dp(80),
            font_size=FONT_SIZE_SMALL,
            color=COLOR_TEXT,
            halign="right",
            valign="middle",
        )
        speed_lbl.bind(size=self._update_text_size)  # type: ignore[attr-defined]
        speed_layout.add_widget(speed_lbl)

        self.speed_slider = Slider(
            min=0.1,
            max=2.0,
            value=0.8,
            step=0.1,
            size_hint=(1, None),
            height=dp(40),
        )
        self.speed_slider.bind(value=self._update_speed_label)  # type: ignore[attr-defined]
        speed_layout.add_widget(self.speed_slider)

        self.speed_label = Label(
            text="0.8s",
            size_hint=(None, 1),
            width=dp(50),
            font_size=FONT_SIZE_SMALL,
            color=COLOR_TEXT,
            halign="left",
            valign="middle",
        )
        self.speed_label.bind(size=self._update_text_size)  # type: ignore[attr-defined]
        speed_layout.add_widget(self.speed_label)

        controls.add_widget(speed_layout)

        # Step indicator
        self.step_indicator = Label(
            text=f"Step 1/{len(self.steps)}",
            font_size=FONT_SIZE_SMALL,
            size_hint=(1, None),
            height=dp(25),
            color=COLOR_TEXT,
            halign="center",
            valign="middle",
        )
        self.step_indicator.bind(size=self._update_text_size)  # type: ignore[attr-defined]
        controls.add_widget(self.step_indicator)

        return controls

    def _update_speed_label(self, instance, value):
        self.speed_label.text = f"{value:.1f}s"

    def update_display(self):
        """Update display based on current step."""
        if self.current_step >= len(self.steps):
            self.current_step = len(self.steps) - 1
        if self.current_step < 0:
            self.current_step = 0

        step = self.steps[self.current_step]

        # Update input array
        current_idx = step.i if step.i >= 0 else -1
        self.input_widget.update_state(current_idx, set())

        # Update stack
        pushing_digit = step.digit if step.is_pushing else None
        self.stack_widget.update_stack(
            step.stack,
            highlight_top=step.highlight_top,
            is_popping=step.is_popping,
            is_pushing=step.is_pushing,
            pushing_digit=pushing_digit,
        )

        # Update labels
        self.step_label.text = step.description
        self.condition_label.text = step.condition_info or ""
        self.step_indicator.text = f"Step {self.current_step + 1}/{len(self.steps)}"

        # Update buttons
        self.prev_btn.disabled = self.current_step == 0
        self.next_btn.disabled = self.current_step >= len(self.steps) - 1

    def next_step(self, *args):
        """Go to next step."""
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.update_display()
        else:
            self.stop_play()

    def prev_step(self, *args):
        """Go to previous step."""
        if self.current_step > 0:
            self.current_step -= 1
            self.update_display()

    def reset(self, *args):
        """Reset to first step."""
        self.stop_play()
        self.current_step = 0
        self.update_display()

    def toggle_play(self, *args):
        """Toggle play/pause."""
        if self.is_playing:
            self.stop_play()
        else:
            self.start_play()

    def start_play(self):
        """Start automatic playback."""
        self.is_playing = True
        self.play_btn.text = "⏸️ Pause"
        self._schedule_next()

    def stop_play(self):
        """Stop automatic playback."""
        self.is_playing = False
        self.play_btn.text = "▶️ Play"
        if self.play_event:
            self.play_event.cancel()
            self.play_event = None

    def _schedule_next(self):
        """Schedule next step."""
        if self.is_playing:
            interval = self.speed_slider.value
            self.play_event = Clock.schedule_once(self._auto_next, interval)

    def _auto_next(self, dt):
        """Callback for automatic advance."""
        if self.is_playing:
            if self.current_step < len(self.steps) - 1:
                self.next_step()
                self._schedule_next()
            else:
                self.stop_play()


class MaxPowerVisualizerApp(App):
    """Main Kivy application."""

    def build(self):
        Window.clearcolor = COLOR_BG
        Window.size = (800, 750)
        return VisualizerWidget()


if __name__ == "__main__":
    MaxPowerVisualizerApp().run()
