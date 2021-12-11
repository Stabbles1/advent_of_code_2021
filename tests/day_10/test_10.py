from day_10.main import input_to_chunk_lines, calculate_corrupt_score
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

def test_input_to_chunk_lines():
    chunk_lines = input_to_chunk_lines(test_input)
    assert len(chunk_lines) == 10
    assert chunk_lines[0].line == "[({(<(())[]>[[{[]{<()<>>"
    assert chunk_lines[4].line == "[[<[([]))<([[{}[[()]]]"

def test_chunk_line_can_identify_corrupt():
    valid_line  = ChunkLine("[({(<(())[]>[[{[]{<()<>>")
    corrupt_line  = ChunkLine("{([(<{}[<>[]}>{[]{[(<()>")

    assert valid_line.is_corrupt() == False
    assert corrupt_line.is_corrupt() == True
    assert corrupt_line.corrupt_character == "}"

def test_part_1():
    chunk_lines = input_to_chunk_lines(test_input)
    assert(calculate_corrupt_score(chunk_lines)) == 26397

