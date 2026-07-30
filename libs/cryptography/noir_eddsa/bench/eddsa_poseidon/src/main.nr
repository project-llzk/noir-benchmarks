use eddsa::eddsa_verify;
use poseidon::poseidon::PoseidonHasher;

fn main(
    pub_key_x: Field,
    pub_key_y: Field,
    signature_s: Field,
    signature_r8_x: Field,
    signature_r8_y: Field,
    message: Field,
) -> pub bool {
    eddsa_verify::<PoseidonHasher>(
        pub_key_x,
        pub_key_y,
        signature_s,
        signature_r8_x,
        signature_r8_y,
        message,
    )
}
