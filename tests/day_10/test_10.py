from day_10.main import input_to_program
from day_10.chunk_line import ChunkLine

test_input = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


def test_input_to_input_to_program():
    program = input_to_program(test_input)
    assert len(program.chunk_lines) == 10
    assert program.chunk_lines[0].line == "[({(<(())[]>[[{[]{<()<>>"
    assert program.chunk_lines[4].line == "[[<[([]))<([[{}[[()]]]"


def test_chunk_line_can_identify_corrupt():
    valid_line = ChunkLine("[({(<(())[]>[[{[]{<()<>>")
    corrupt_line = ChunkLine("{([(<{}[<>[]}>{[]{[(<()>")

    assert valid_line.is_corrupt() == False
    assert corrupt_line.is_corrupt() == True
    assert corrupt_line.corrupt_character == "}"


def test_part_1():
    program = input_to_program(test_input)
    assert (program.calculate_corrupt_score()) == 26397


def test_program_can_remove_corrupt_lines():
    program = input_to_program(test_input)
    program.remove_corrupt_lines()
    assert len(program.chunk_lines) == 5


def test_chunk_line_can_complete_sequence():
    incomplete_line = ChunkLine("[({(<(())[]>[[{[]{<()<>>")
    assert incomplete_line.get_completion_sequence() == "}}]])})]"


def test_chunk_line_can_calculate_completion_score():
    incomplete_line = ChunkLine("<{([{{}}[<[[[<>{}]]]>[]]")
    assert incomplete_line.get_completion_sequence() == "])}>"
    assert incomplete_line.completion_score() == 294


def test_part_2():
    program = input_to_program(test_input)
    assert program.calculate_incomplete_score() == 288957
