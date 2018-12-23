import regex
import colored
from colored import stylize
from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError


question_style = style_from_dict(
    {
        Token.QuestionMark: "#E91E63 bold",
        Token.Selected: "#673AB7 bold",
        Token.Instruction: "",  # default
        Token.Answer: "#2196f3 bold",
        Token.Question: "",
    }
)

questions = [
    {
        "type": "list",
        "name": "task",
        "message": "What would you like to do?",
        "choices": [
            {"key": "s", "name": "SSH into server", "value": "ssh"},
            {"key": "e", "name": "Exit", "value": "exit"},
        ],
    }
]

print(stylize("Hello!", colored.fg("green")))
print(stylize("Reading config file...", colored.fg("green")))
answers = prompt(questions, style=question_style)
if answers['task'] == 'ssh':
    question_2 = [
    {
        "type": "list",
        "name": "task",
        "message": "How would you like to What would you like to do?",
        "choices": [
            {"key": "s", "name": "SSH into server", "value": "ssh"},
            {"key": "e", "name": "Exit", "value": "exit"},
        ],
    }




