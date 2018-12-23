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
            {"key": "s", "name": "SSH into server", "value": "ssh"}
        ],
    },
    {
        "type": "list",
        "name": "server_selection_1",
        "message": "Which server would you like to target?",
        "choices": [
            {"key": "1", "name": "FROM_HISTORY", "value": "ssh"},
            {"key": "dns", "name": "Type DNS", "value": "dns"},
            {"key": "aws", "name": "Query AWS", "value": "query"},
        ],
    },
    {
        "type": "input",
        "name": "server_selection_2.1",
        "message": "Type DNS Name?",
        'when': lambda answers: answers['server_selection_1']=='dns'
    },
    {
        "type": "list",
        "name": "server_selection_2.2.1",
        "message": "AWS Profile?",
        "choices": [
            {"key": "default", "name": "FROM_HISTORY", "value": "ssh"},
        ],
        'when': lambda answers: answers['server_selection_1'] == 'aws'
    },
    {
        "type": "input",
        "name": "server_selection_2.2.2",
        "message": "Instance name?",
        'when': lambda answers: answers['server_selection_1'] == 'aws'
    }
]

print(stylize("Hello!", colored.fg("green")))
print(stylize("Reading config file...", colored.fg("green")))
answers = prompt(questions, style=question_style)


