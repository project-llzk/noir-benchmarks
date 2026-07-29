use poseidon::poseidon::bn254;

fn main(input: [Field; 8]) -> pub Field {
    bn254::sponge(input)
}
