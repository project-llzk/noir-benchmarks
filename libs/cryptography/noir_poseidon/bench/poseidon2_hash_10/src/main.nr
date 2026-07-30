use poseidon::poseidon2::Poseidon2;

fn main(input: [Field; 10]) -> pub Field {
    Poseidon2::hash(input, input.len())
}
