"""Generates output.gif: a retro boot sequence + quest-log card for the profile README."""
import gifos

t = gifos.Terminal(width=640, height=260, xpad=10, ypad=10)
t.set_fps(15)

# --- boot sequence ---------------------------------------------------------
t.toggle_show_cursor(False)
boot = [
    "[  \x1b[92mOK\x1b[0m  ] Booting DEVOS v2026.10",
    "[  \x1b[92mOK\x1b[0m  ] Loading Flutter, React, Node, AWS",
    "[  \x1b[92mOK\x1b[0m  ] Mounting side projects",
    "[  \x1b[92mOK\x1b[0m  ] Player 1 ready",
]
for i, line in enumerate(boot, start=1):
    t.gen_text(line, row_num=i, count=6)
t.clone_frame(10)
t.clear_frame()

# --- prompt + command ------------------------------------------------------
t.set_prompt("\x1b[92mdev\x1b[0m@\x1b[96mdevos\x1b[0m:\x1b[94m~\x1b[0m$ ")
t.toggle_show_cursor(True)
t.gen_prompt(row_num=1)
t.gen_typing_text("whoami --quest-log", row_num=1, contin=True)
t.clone_frame(8)

# --- output card -----------------------------------------------------------
card = [
    "\x1b[93mDev Bathani\x1b[0m  |  Full Stack Engineer",
    "\x1b[90m--------------------------------------------\x1b[0m",
    "\x1b[92mNOW  \x1b[0m LIWIP (Full Stack Engineer)",
    "\x1b[92mPREV \x1b[0m Polygram (Co-Founder, AI dev platform)",
    "\x1b[92mPREV \x1b[0m CleverTap (Technical Account Manager)",
    "\x1b[92mPREV \x1b[0m OTPless (Senior Solution Engineer)",
    "\x1b[96mSTACK\x1b[0m Flutter React TS Node AWS Python",
    "\x1b[95mSIDE \x1b[0m Govyrl, Polygram, Flame games",
]
for i, line in enumerate(card, start=2):
    t.gen_text(line, row_num=i, count=3)

t.gen_prompt(row_num=len(card) + 2)
t.clone_frame(40)
t.gen_gif()
