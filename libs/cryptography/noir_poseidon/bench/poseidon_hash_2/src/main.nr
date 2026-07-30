use poseidon::poseidon::bn254;

fn main(input: [Field; 2]) -> pub Field {
    bn254::hash_2(input)
}
