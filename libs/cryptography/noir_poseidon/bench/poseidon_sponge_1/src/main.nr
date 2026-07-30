use poseidon::poseidon::bn254;

fn main(input: [Field; 1]) -> pub Field {
    bn254::sponge(input)
}
