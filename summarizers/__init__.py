"""
Add new summarizer here:
"""

from summarizers import gpt3, accel_brain

SUMMARIZE = {
    "gpt3": gpt3.summarize,
    "accel_brain": accel_brain.summarize,
}
