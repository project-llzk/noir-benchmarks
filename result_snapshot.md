Machine specs = 2023 MacBook Pro, Apple M2 Pro, 16GB, 495GB SSD, macOS v26.6
nthreads = 1
timeout = 600
noir_llzk commit = a1013fb69e913cc33e248434ebede785e9dc6790
nargo version = 1.0.0-beta.19

|Benchmark|Result|Nargo Compile Time (sec)|ACIR2LLZK Time (sec)|Total Time (sec)|Error Message|
| :--- | :--- | :--- | :--- | :--- | :--- |
|aztec-packages/parity-base|success|6.317959|7.252871|13.570829|
|aztec-packages/parity-root|error|1.176774|0.018638|1.195413|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|aztec-packages/private-kernel-init|error|0.936285|0.031305|0.967590|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|aztec-packages/private-kernel-inner|error|1.406454|0.041294|1.447747|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|aztec-packages/private-kernel-reset|error|4.697665|0.088381|4.786046|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|aztec-packages/rollup-block-merge|error|1.148926|0.017711|1.166637|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|aztec-packages/rollup-block-root|error|1.204629|0.018054|1.222683|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|aztec-packages/rollup-checkpoint-root|error|297.361173|0.000000|297.361173|nargo compile: exit code -9
|aztec-packages/rollup-root|error|1.406287|0.177523|1.583810|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|aztec-packages/rollup-tx-base-private|error|15.725262|0.277139|16.002400|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|aztec-packages/rollup-tx-base-public|error|52.599675|0.276613|52.876288|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|aztec-packages/rollup-tx-merge|error|1.216239|0.017699|1.233938|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|interfold-config|success|0.451341|0.162278|0.613619|
|interfold-dkg/e_sm_share_computation|success|2.743969|0.702316|3.446285|
|interfold-dkg/pk|success|2.743969|0.043688|2.787657|
|interfold-dkg/share_decryption|success|2.743969|0.558261|3.302230|
|interfold-dkg/share_encryption|success|2.743969|1.147126|3.891095|
|interfold-dkg/sk_share_computation|success|2.743969|0.370674|3.114643|
|interfold-recursive-aggregation/c2ab_fold|error|0.962487|0.015361|0.977848|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|interfold-recursive-aggregation/c3_fold|error|0.962487|0.013986|0.976473|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|interfold-recursive-aggregation/c3_fold_kernel|error|0.962487|0.013672|0.976159|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|interfold-recursive-aggregation/c3ab_fold|error|0.962487|0.013678|0.976165|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|interfold-recursive-aggregation/c4ab_fold|error|0.962487|0.013288|0.975775|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|interfold-recursive-aggregation/c6_fold|error|0.962487|0.013364|0.975851|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|interfold-recursive-aggregation/c6_fold_kernel|error|0.962487|0.013365|0.975852|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|interfold-recursive-aggregation/decryption_aggregator|error|0.962487|0.016259|0.978746|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|interfold-recursive-aggregation/dkg_aggregator|error|0.962487|0.016395|0.978882|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|interfold-recursive-aggregation/node_fold|error|0.962487|0.013739|0.976226|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|interfold-recursive-aggregation/nodes_fold|error|0.962487|0.013716|0.976203|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|interfold-recursive-aggregation/nodes_fold_kernel|error|0.962487|0.012954|0.975441|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|interfold-threshold/decrypted_shares_aggregation|success|1.999177|0.959912|2.959089|
|interfold-threshold/pk_aggregation|success|1.999177|0.143759|2.142936|
|interfold-threshold/pk_generation|success|1.999177|0.721776|2.720953|
|interfold-threshold/share_decryption|success|1.999177|0.761016|2.760193|
|interfold-threshold/user_data_encryption|error|1.999177|0.014668|2.013845|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|interfold-threshold/user_data_encryption_ct0|success|1.999177|0.722409|2.721586|
|interfold-threshold/user_data_encryption_ct1|success|1.999177|0.586426|2.585603|
|noir_base64_decode_610|success|0.200476|13.650043|13.850520|
|noir_base64_decode_610_no_pad|success|0.143198|0.023317|0.166515|
|noir_base64_decode_610_var|success|0.689397|44.339111|45.028508|
|noir_base64_decode_610_var_no_pad|success|0.525988|40.414686|40.940674|
|noir_base64_encode_610|success|0.253582|3.409768|3.663350|
|noir_base64_encode_610_no_pad|success|0.259548|3.421846|3.681393|
|noir_base64_encode_610_url_safe|success|0.246110|3.412030|3.658141|
|noir_base64_encode_610_url_safe_var|success|0.649430|10.558126|11.207556|
|noir_base64_encode_610_var|success|0.731095|10.721914|11.453008|
|noir_base64_encode_610_var_no_pad|success|0.646796|10.767978|11.414774|
|noir_bigcurve_bn254_add|success|0.781346|1.013799|1.795146|
|noir_bigcurve_bn254_eq|success|0.391746|0.022370|0.414116|
|noir_bigcurve_bn254_evaluate_linear_expression|success|10.482148|8.423057|18.905205|
|noir_bigcurve_bn254_hash_to_curve|success|0.475485|0.251833|0.727318|
|noir_bigcurve_bn254_mul|success|6.855429|5.364350|12.219778|
|noir_bigcurve_bn254_neg|success|0.358785|0.017458|0.376243|
|noir_bigcurve_bn254_sub|success|0.790808|0.980026|1.770834|
|noir_bigcurve_bn254_validate_on_curve|success|0.397870|0.114072|0.511942|
|noir_bignum_bn254_fq_add|success|0.296733|0.023494|0.320227|
|noir_bignum_bn254_fq_batch_invert_10|success|0.322652|0.115651|0.438304|
|noir_bignum_bn254_fq_derive_from_seed|success|0.332723|0.124738|0.457461|
|noir_bignum_bn254_fq_div|success|0.327010|0.098244|0.425254|
|noir_bignum_bn254_fq_eq|success|0.279207|0.021583|0.300790|
|noir_bignum_bn254_fq_from_be_bytes|success|0.292719|0.016381|0.309099|
|noir_bignum_bn254_fq_from_field|success|0.278834|0.019699|0.298533|
|noir_bignum_bn254_fq_mul|success|0.311836|0.075793|0.387629|
|noir_bignum_bn254_fq_sub|success|0.286836|0.021716|0.308552|
|noir_bignum_bn254_fq_to_be_bytes|success|0.291805|0.018438|0.310243|
|noir_bignum_u2048_mul|success|0.326696|0.089709|0.416405|
|noir_bignum_u256_cmp|success|0.292621|0.020123|0.312745|
|noir_bignum_u256_evaluate_quadratic_expression_3|success|0.319884|0.062882|0.382767|
|noir_bignum_u256_udiv|success|0.303076|0.054130|0.357206|
|noir_bignum_u256_udiv_mod|success|0.292266|0.054771|0.347037|
|noir_bignum_u256_validate_in_range|success|0.281729|0.015363|0.297092|
|noir_eddsa_poseidon|success|0.658636|0.602104|1.260740|
|noir_eth-proofs_get_account|timeout|11.941381|602.160173|614.101555|acir2llzk timeout
|noir_eth-proofs_get_header|success|3.335057|320.150017|323.485074|
|noir_eth-proofs_get_log|error|29.268965|255.413518|284.682483|acir2llzk: exit code -9
|noir_eth-proofs_get_receipt|timeout|18.405375|602.398392|620.803767|acir2llzk timeout
|noir_eth-proofs_get_storage|error|16.882433|346.800106|363.682540|acir2llzk: exit code -9
|noir_eth-proofs_get_storage_recursive|error|16.877550|351.339448|368.216998|acir2llzk: exit code -9
|noir_eth-proofs_get_transaction|timeout|23.330480|602.389677|625.720157|acir2llzk timeout
|noir_json_parser_get_array_length|success|0.677789|0.025332|0.703121|
|noir_json_parser_get_nested_object_number|success|0.581333|0.017509|0.598842|
|noir_json_parser_get_number|success|0.560257|0.015474|0.575730|
|noir_json_parser_get_string|success|0.571259|0.026336|0.597595|
|noir_json_parser_parse_16kb|error|105.578583|337.797873|443.376456|acir2llzk: exit code -9
|noir_json_parser_parse_1kb|success|2.296506|282.528558|284.825064|
|noir_json_parser_parse_2kb|timeout|4.415210|601.565668|605.980878|acir2llzk timeout
|noir_json_parser_parse_4kb|error|11.461049|431.439825|442.900874|acir2llzk: exit code -9
|noir_json_parser_parse_512b|success|1.105496|94.710431|95.815927|
|noir_json_parser_parse_8kb|error|32.798568|335.928194|368.726762|acir2llzk: exit code -9
|noir_keccak256_1|success|0.147381|4.391695|4.539076|
|noir_keccak256_100|success|0.110773|3.992704|4.103477|
|noir_keccak256_135|success|0.114852|3.874145|3.988998|
|noir_keccak256_256|success|0.162310|16.699816|16.862126|
|noir_mimc_bn254_1|success|0.098040|0.026977|0.125017|
|noir_mimc_bn254_10|success|0.184338|0.124987|0.309325|
|noir_mimc_bn254_100|success|4.749550|1.314892|6.064442|
|noir_poseidon2_hash_1|success|0.110562|0.020178|0.130740|
|noir_poseidon2_hash_10|success|0.108538|0.020796|0.129334|
|noir_poseidon2_hash_2|success|0.108233|0.020463|0.128696|
|noir_poseidon2_hash_20|success|0.109394|0.022012|0.131406|
|noir_poseidon2_hash_4|success|0.112367|0.020475|0.132842|
|noir_poseidon2_hash_8|success|0.107310|0.020691|0.128000|
|noir_poseidon_hash_1|success|0.124017|0.034298|0.158315|
|noir_poseidon_hash_2|success|0.145182|0.065344|0.210526|
|noir_poseidon_hash_4|success|0.159462|0.077437|0.236899|
|noir_poseidon_hash_8|success|0.192834|0.111580|0.304414|
|noir_poseidon_sponge_1|success|0.158615|0.073370|0.231985|
|noir_poseidon_sponge_16|success|0.378726|0.196479|0.575205|
|noir_poseidon_sponge_32|success|0.674945|0.363757|1.038702|
|noir_poseidon_sponge_4|success|0.185390|0.075356|0.260746|
|noir_poseidon_sponge_8|success|0.242275|0.116860|0.359135|
|noir_sha256_1|success|0.091004|0.084495|0.175499|
|noir_sha256_200|success|0.110728|0.201838|0.312566|
|noir_sha256_511|success|0.146357|0.346766|0.493124|
|noir_sha256_512|success|0.147695|0.357134|0.504829|
|noir_sha512_1_block|timeout|1.200762|601.532094|602.732856|acir2llzk timeout
|noir_sha512_2_blocks|timeout|2.159985|602.038931|604.198916|acir2llzk timeout
|noir_sha512_3_blocks|timeout|2.867692|602.248490|605.116182|acir2llzk timeout
|noir_sha512_4_blocks|error|3.828858|389.927647|393.756505|acir2llzk: exit code -9
|noir_sha512_compression|timeout|1.346378|601.592453|602.938831|acir2llzk timeout
|noir_sha512_var_1_block|timeout|1.233134|601.298761|602.531895|acir2llzk timeout
|noir_sha512_var_2_blocks|timeout|2.018528|601.925537|603.944064|acir2llzk timeout
|noir_sha512_var_3_blocks|timeout|2.825036|602.259572|605.084609|acir2llzk timeout
|noir_sha512_var_4_blocks|error|3.762479|353.110214|356.872693|acir2llzk: exit code -9
|noir_string_search_match_1024_128|success|0.229898|2.060001|2.289899|
|noir_string_search_match_128_32|success|0.101308|0.380405|0.481713|
|noir_string_search_match_32_32|success|0.086935|0.376780|0.463715|
|noir_string_search_match_512_64|success|0.113234|0.739192|0.852426|
|payy/agg_agg|error|4.911993|0.100256|5.012248|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|payy/agg_final|error|4.911993|0.014107|4.926100|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|payy/agg_utxo|error|4.911993|0.048858|4.960851|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|payy/burn|success|4.911993|0.873054|5.785047|
|payy/erc20_transfer|success|1.566551|525.950394|527.516945|
|payy/migrate|success|4.911993|0.053945|4.965938|
|payy/mint|success|4.911993|0.976612|5.888604|
|payy/points|success|4.911993|0.023135|4.935128|
|payy/signature|success|4.911993|0.017496|4.929489|
|payy/transfer_claim|success|4.911993|1.029949|5.941941|
|payy/transfer_send|success|4.911993|0.889438|5.801430|
|payy/utxo|success|4.911993|0.034632|4.946624|
|sparq_IEEE754_f128_div|success|0.154395|0.038676|0.193071|
|sparq_IEEE754_f128_from_u128|success|0.096985|0.023072|0.120056|
|sparq_IEEE754_f128_mul|success|0.105067|0.040097|0.145164|
|sparq_IEEE754_f16_add|success|0.100359|0.032742|0.133101|
|sparq_IEEE754_f16_compare|success|0.093085|0.018854|0.111939|
|sparq_IEEE754_f16_mul|success|0.097455|0.033877|0.131332|
|sparq_IEEE754_f32_div|success|0.098033|0.033840|0.131873|
|sparq_IEEE754_f32_round_ties_even|success|0.097515|0.030974|0.128489|
|sparq_IEEE754_f64_sqrt|success|0.098771|0.031533|0.130304|
|sparq_IEEE754_f64_to_i64|success|0.093291|0.026610|0.119901|
|sparq_XPath_date_add_duration|success|1.036893|0.033982|1.070875|
|sparq_XPath_hash_sha256_64|success|0.234271|0.047212|0.281483|
|sparq_XPath_json_array_number_512b|success|0.985478|98.357324|99.342802|
|sparq_XPath_numeric_int_ops|success|0.266000|0.022092|0.288092|
|sparq_XPath_regex_replace_literal|success|0.234567|0.015932|0.250498|
|sparq_XPath_sequence_sort_32|success|0.686813|0.600783|1.287596|
|sparq_XPath_string_contains_64_8|success|0.243764|0.014955|0.258719|
|sparq_XPath_string_tokenize_64|success|0.253288|0.014982|0.268270|
|stellar_confidential_token/circuit_register|success|0.203332|0.134676|0.338008|
|stellar_confidential_token/circuit_revoke_spender|success|0.203332|0.392864|0.596196|
|stellar_confidential_token/circuit_set_spender|success|0.203332|0.424515|0.627847|
|stellar_confidential_token/circuit_spender_transfer|success|0.203332|0.431119|0.634451|
|stellar_confidential_token/circuit_transfer|success|0.203332|0.412697|0.616029|
|stellar_confidential_token/circuit_withdraw|success|0.203332|0.373945|0.577277|
|stellar_confidential_token/gadget_assert_on_curve|success|0.203332|0.015672|0.219004|
|stellar_confidential_token/gadget_commit|success|0.203332|0.233480|0.436812|
|stellar_confidential_token/gadget_ecdh|success|0.203332|0.124524|0.327856|
|stellar_confidential_token/gadget_encrypt_amount|success|0.203332|0.018844|0.222175|
|stellar_confidential_token/gadget_poseidon_with_domain|success|0.203332|0.018785|0.222117|
|stellar_confidential_token/gadget_sponge_squeeze_2|success|0.203332|0.018076|0.221408|
|stellar_confidential_token/gadget_vk_from_sk|success|0.203332|0.018620|0.221952|
|wei-as-decimal_from_u128|success|0.993485|0.070401|1.063886|
|wei-as-decimal_to_wad|success|0.887418|0.014843|0.902262|
|wei-as-decimal_truncate|success|0.889808|0.016123|0.905931|
|wei-as-decimal_wad_add|success|0.911474|0.014922|0.926396|
|wei-as-decimal_wad_div|success|0.919407|0.022747|0.942154|
|wei-as-decimal_wad_mul|success|0.887808|0.024179|0.911987|
|wei-as-decimal_wad_mul_div|success|0.920709|0.023425|0.944134|
|wei-as-decimal_wad_sub|success|0.882630|0.016064|0.898693|
|zerosats_ciphera/agg_agg|error|3.292994|0.015642|3.308637|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|zerosats_ciphera/agg_escrow|error|3.292994|0.042429|3.335423|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|zerosats_ciphera/agg_utxo|error|3.292994|0.041104|3.334098|acir2llzk: UnsupportedOpcode(BLACKBOX::RECURSIVE_AGGREGATION)|
|zerosats_ciphera/escrow|success|3.292994|1.183985|4.476979|
|zerosats_ciphera/migrate|success|3.292994|0.062021|3.355015|
|zerosats_ciphera/signature|success|3.292994|0.020638|3.313632|
|zerosats_ciphera/signature32|success|3.292994|0.021703|3.314697|
|zerosats_ciphera/signature32sha|success|3.292994|0.043849|3.336844|
|zerosats_ciphera/timelock|success|3.292994|0.306195|3.599189|
|zerosats_ciphera/utxo|success|3.292994|0.024829|3.317823|
|zkpassport_date_add_days|success|0.081618|0.031531|0.113149|
|zkpassport_date_add_months|success|0.074178|0.023450|0.097628|
|zkpassport_date_duration_in_days|success|0.089360|0.048879|0.138240|
|zkpassport_date_from_bytes_long_year|success|0.075256|0.019083|0.094339|
|zkpassport_date_from_bytes_short_year|success|0.073627|0.021716|0.095343|
|zkpassport_date_from_timestamp|success|0.080566|0.029332|0.109899|
|zkpassport_date_gt|success|0.089405|0.056607|0.146012|
|zkpassport_date_sub_days|success|0.081972|0.032272|0.114244|
|zkpassport_date_to_bytes|success|0.076434|0.019601|0.096035|
|zkpassport_date_to_timestamp|success|0.082194|0.035752|0.117945|
