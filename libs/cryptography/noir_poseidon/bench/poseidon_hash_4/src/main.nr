use poseidon::poseidon::bn254;

fn main(input: [Field; 4]) -> pub Field {
    bn254::hash_4(input)
}
