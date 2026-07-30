use poseidon::poseidon::bn254;

fn main(input: [Field; 16]) -> pub Field {
    bn254::sponge(input)
}
