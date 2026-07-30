use sha512::sha512_compression;

fn msg_u8_to_u64(msg: [u8; 128]) -> [u64; 16] {
    let mut msg64: [u64; 16] = [0; 16];

    for i in 0..16 {
        let mut msg_field: Field = 0;
        for j in 0..8 {
            msg_field = msg_field * 256 + msg[128 - 8 * (i + 1) + j] as Field;
        }

        msg64[15 - i] = msg_field as u64;
    }

    msg64
}

fn main(input: [u8; 128], h: [u64; 8]) -> pub [u64; 8] {
    sha512_compression(msg_u8_to_u64(input), h)
}
