use poseidon::poseidon::bn254;

fn main(input: [Field; 8]) -> pub Field {
    bn254::hash_8(input)
}
