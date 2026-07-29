use poseidon::poseidon2::Poseidon2;

fn main(input: [Field; 1]) -> pub Field {
    Poseidon2::hash(input, input.len())
}
