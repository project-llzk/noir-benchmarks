mod circuit;

#[test(should_fail)]
fn test_set_code_invalid_small() {
    // code pegs should be in the range [0,5]
    let code = [0, 0, 0, -1];
    let _ = circuit::set_code(987654321, code);
}

#[test(should_fail)]
fn test_set_code_invalid_large() {
    // code pegs should be in the range [0,5]
    let code = [0, 6, 0, 0];
    let _ = circuit::set_code(987654321, code);
}

fn main(
    codemaker_nonce: Field,
    codemaker_code: [Field; 4],
    guess: pub [Field; 4],
    expected_correct: pub Field,
    expected_partial: pub Field,
) {
    let code_hash = circuit::set_code(codemaker_nonce, codemaker_code);
    let (correct, partial) =
        circuit::make_guess_with_checks(codemaker_nonce, codemaker_code, code_hash, guess);

    assert(correct == expected_correct);
    assert(partial == expected_partial);
}
