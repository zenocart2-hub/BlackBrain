"""
BlackBrain Brain Engine
----------------------
Main logic engine for problem solving, decision making,
and structured responses (non-generic, logical).
"""

from datetime import datetime
from typing import Dict, List

# ----------------------------------------
# CORE BRAIN RESPONSE ENGINE
# ----------------------------------------

def decision_brain(problem: str) -> Dict:
    """
    Used for decision making problems.
    Example: Job vs Business, Buy phone A or B
    """
    return {
        "type": "decision",
        "problem": problem,
        "analysis": {
            "pros": [
                "Short-term clarity",
                "Predictable outcome"
            ],
            "cons": [
                "Risk involved",
                "Time & effort required"
            ],
            "risk_level": "Medium",
            "logic": "Decision should be based on long-term stability and skill growth"
        },
        "final_suggestion": (
            "Choose the option that improves your skills and income stability "
            "over the next 12 months, not instant comfort."
        )
    }


def problem_breaker(problem: str) -> Dict:
    """
    Breaks a big life problem into root causes and actions
    """
    return {
        "type": "problem_breaker",
        "problem": problem,
        "root_causes": [
            "Lack of clarity",
            "Poor daily structure",
            "Emotional overload"
        ],
        "what_you_control": [
            "Daily routine",
            "Information intake",
            "Effort consistency"
        ],
        "7_day_action_plan": [
            "Day 1: Write exact problem clearly",
            "Day 2: Remove 1 distraction",
            "Day 3: Fix sleep & wake time",
            "Day 4: Complete 1 hard task",
            "Day 5: Learn one missing skill",
            "Day 6: Review progress",
            "Day 7: Decide next direction"
        ]
    }


def money_brain(amount: int) -> Dict:
    """
    Money planning logic (India-focused)
    """
    return {
        "type": "money_brain",
        "amount": amount,
        "analysis": {
            "avoid": [
                "Impulse buying",
                "Online scams",
                "Fake get-rich-quick schemes"
            ],
            "recommended_use": [
                "Skill learning",
                "Emergency savings",
                "Low-risk experiments"
            ],
            "logic": (
                "Money grows when combined with skill and patience, "
                "not shortcuts."
            )
        },
        "suggested_split": {
            "savings": f"₹{int(amount * 0.4)}",
            "learning": f"₹{int(amount * 0.4)}",
            "experiments": f"₹{int(amount * 0.2)}"
        }
    }


def study_brain(subject: str) -> Dict:
    """
    Study diagnosis and planning
    """
    return {
        "type": "study_brain",
        "subject": subject,
        "diagnosis": [
            "Concept clarity missing",
            "Revision inconsistency",
            "No test analysis"
        ],
        "solution": [
            "Study concepts before memorizing",
            "Revise daily for 30 minutes",
            "Analyze mistakes weekly"
        ],
        "7_day_study_plan": [
            "Day 1–2: Basics",
            "Day 3–4: Examples",
            "Day 5: Practice",
            "Day 6: Mock test",
            "Day 7: Analysis"
        ]
    }


def no_bullshit_mode(problem: str) -> Dict:
    """
    Straight-forward logical response (no sugar coating)
    """
    return {
        "type": "no_bullshit",
        "problem": problem,
        "truth": (
            "You are not lazy. You are avoiding discomfort. "
            "Discomfort is required for growth."
        ),
        "action": [
            "Stop overthinking",
            "Do the hardest task first",
            "Repeat daily without motivation"
        ]
    }


# ----------------------------------------
# MAIN ENTRY FUNCTION
# ----------------------------------------

def run_brain_engine(
    question: str,
    mode: str = "basic"
) -> Dict:
    """
    Main brain router based on mode
    """
    if mode == "decision":
        return decision_brain(question)

    if mode == "problem":
        return problem_breaker(question)

    if mode == "money":
        return money_brain(int(question))

    if mode == "study":
        return study_brain(question)

    if mode == "nobullshit":
        return no_bullshit_mode(question)

    # Default basic response
    return {
        "type": "basic",
        "question": question,
        "answer": (
            "Explain your problem clearly. "
            "Clarity itself solves 50% of problems."
        ),
        "timestamp": datetime.utcnow().isoformat()
    }