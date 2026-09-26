# CONNECTIONS — experiment source inventory

Generated: 2026-09-26

## Scope

This is a source inventory, not a claim that every matching file is an independent experiment. Paths were collected from the complete Git trees of the three repositories and filtered by experimental/research naming signals.

## Counts

- OMEGA-LAB: 393
- ORISIK: 234
- ARCHIVE: 2
- Total candidate records: 629

## Rule

Before copying anything into CONNECTIONS, each candidate must be classified as:
- EXPERIMENT
- RESULT
- PROTOCOL
- AUDIT
- HISTORY
- ARCHIVE/SOURCE
- NON-EXPERIMENT

No source is deleted or rewritten.

## Machine-readable inventory

```json
{
  "generated": "2026-09-26",
  "criteria": "blob paths containing experiment/experiments/test/research/simulation/study/analysis",
  "sources": {
    "OMEGA-LAB": [
      {
        "path": "00_CORE/EXPERIMENTS/OMEGA_FULL_RUN_2026-09-12.md",
        "sha": "5b64a12bd58002b190976d8ab3e4348ba202ce07"
      },
      {
        "path": "00_CORE/EXPERIMENTS/OMEGA_REAL_1_CausRCA_PROTOCOL_v1.0.md",
        "sha": "6b62ac428d5f83b540f06b5da536ad08e6129601"
      },
      {
        "path": "00_CORE/EXPERIMENTS/OMEGA_TEST_10_DIRECT_INTERVENTION_2026-09-12.md",
        "sha": "526a48d9bd235bf1c5db3f7b943543d197982fb5"
      },
      {
        "path": "00_CORE/EXPERIMENTS/OMEGA_TEST_11_BOUNDARY_RELATIONAL_COUNTERFACTUAL_2026-09-12.md",
        "sha": "d9cc5bbfd57e69c2294a9b058fd7fd7f15667634"
      },
      {
        "path": "00_CORE/EXPERIMENTS/OMEGA_TEST_11_BOUNDARY_RELATIONAL_COUNTERFACTUAL_SUMMARY.csv",
        "sha": "320e5f014ad87d944a48611ece832d7e84f85e6d"
      },
      {
        "path": "00_CORE/EXPERIMENTS/OMEGA_TEST_12_CROSS_FAMILY_FALSIFICATION_2026-09-12.md",
        "sha": "1f6601121e914feb46acefe1287cb61a55e5ad11"
      },
      {
        "path": "00_CORE/EXPERIMENTS/OMEGA_TEST_1_GEOMETRIC_SPIRAL_2026-09-12.md",
        "sha": "2d51fcb97f8b194e6ec5cc22e6e4d41ab707477b"
      },
      {
        "path": "00_CORE/EXPERIMENTS/OMEGA_TEST_2_BOUNDARY_CYCLE_2026-09-12.md",
        "sha": "4887fb0f8aea160846b53f6adae45ebaaddfb2c2"
      },
      {
        "path": "00_CORE/EXPERIMENTS/OMEGA_TEST_3_DYNAMIC_BOUNDARY_2026-09-12.md",
        "sha": "7f0154bce271e797778406529ec11647455111b5"
      },
      {
        "path": "00_CORE/EXPERIMENTS/OMEGA_TEST_4_OPPOSING_INTERACTION_2026-09-12.md",
        "sha": "8b20ff6a3f542ef01ce4aabe147a2c55e7607947"
      },
      {
        "path": "00_CORE/EXPERIMENTS/OMEGA_TEST_5_INTERVENTION_2026-09-12.md",
        "sha": "e8a488277c3ab8c600f93d878cb4f7a23e84be7f"
      },
      {
        "path": "00_CORE/EXPERIMENTS/OMEGA_TEST_6_CROSS_FAMILY_RESULTS_2026-09-12.csv",
        "sha": "be219f58607bffa99d3074eb3c3b517a1536dd9e"
      },
      {
        "path": "00_CORE/EXPERIMENTS/OMEGA_TEST_7_BLIND_ADVERSARIAL_2026-09-12.md",
        "sha": "be32c93873a5385b336dd49c22e44880e1dd3741"
      },
      {
        "path": "00_CORE/EXPERIMENTS/OMEGA_TEST_9_MATCHED_MARGINAL_2026-09-12.md",
        "sha": "750800d9bec4f1846c19045515084ab05d13d9fd"
      },
      {
        "path": "00_CORE/EXPERIMENTS/README.md",
        "sha": "04c7b6ec49afeb660ee73d139a77a5dbfd64737a"
      },
      {
        "path": "00_CORE/OMEGA_RESEARCH_STATE_2026-08-10.md",
        "sha": "a2e59014c82a2a3335d99e6553a52dc9d3d47880"
      },
      {
        "path": "00_CORE/SPACE_SECURITY_TEST_MATRIX_v1.0.md",
        "sha": "10ce8eed17b6215af98b0f0e1c35f95e8e348f08"
      },
      {
        "path": "00_CORE/test_omega_loop_guard.py",
        "sha": "7581866db992c3cfe8a187d96d3346a47fb2c1d2"
      },
      {
        "path": "01_HISTORY/CHAT_ARCHIVES/028-RULE-SPACE-GRAPH-REWRITING-COMPUTATIONAL-EXPERIMENTS.md",
        "sha": "44f5dd4355d491e7a6c3c9ff1d9d6f37fe55303e"
      },
      {
        "path": "01_HISTORY/CHAT_ARCHIVES/ARCHIVE_ANALYSIS-SPACE-ORGANS-SKILLS.md",
        "sha": "119b6912d42678c9db3d4a5565fdb36794a39fba"
      },
      {
        "path": "01_HISTORY/EXPERIMENTS/E-LIGHT-0007-SPECTRAL-NETWORK-RESULTS.md",
        "sha": "14c67090ea120c6a39f7c1dd8d92cdff9fbb39e9"
      },
      {
        "path": "02_EXPERIMENTS/E-ENERGY-0037-SYMMETRIC-BIFURCATION.md",
        "sha": "9c31dc05f13860111b2dafa882dbf9ee5e02ba0d"
      },
      {
        "path": "02_EXPERIMENTS/E-MAGNETIC-0001-ENVIRONMENTAL-POTENTIAL-LIGHTNING-CAPTURE.md",
        "sha": "08ea41817f710bbce05190364f32c45c13e46412"
      },
      {
        "path": "03_EXPERIMENTS/E-LIGHT-0003-COLOR-AS-RELATIONAL-INFORMATION.md",
        "sha": "5880b0d14603bce866ac074e6f6781314d6d1989"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/D_R_VS_W_P_AUDIT_v0.2.md",
        "sha": "5c34054b3bef3fd23cd04af278dd7fc47f5c7d4c"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/D_R_VS_W_P_DEPENDENCY_CLOSURE_v0.2.py",
        "sha": "733194c6063359b396d969e580580d280221a063"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/D_R_VS_W_P_EVALUATOR_RESULT_v0.1_2026-08-28.md",
        "sha": "662f6678d3b7f98db491ac388a0dd83e266f0377"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/D_R_VS_W_P_EXECUTABLE_EVALUATOR_v0.1.py",
        "sha": "1a50716f6685bcea6092aad2e1d9759f64661dc9"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/D_R_W_P_OBSERVATIONAL_MAPPING_v0.1.md",
        "sha": "2888aabce72b30d333fb75b4258f245f15609d21"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/MINIMAL_BASIS_MAPPING_AUDIT_v0.1.md",
        "sha": "97a8450c9fea424a05b28d184d678ee9e4954457"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/MINIMAL_BASIS_NEUTRAL_MACHINE_v0.4.py",
        "sha": "8f5ae44183a8c646edd99f5ddada117fca7d4de3"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/MINIMAL_BASIS_NEUTRAL_MACHINE_v0.4_EXECUTION_2026-08-28.md",
        "sha": "a7a0c59859a5c4b74bcea8bda4267f6424e7f498"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/MINIMAL_BASIS_NEUTRAL_MACHINE_v0.4_EXECUTION_AUDIT_2026-08-28.md",
        "sha": "9b64073c67f50f122374cd680c342823d996452d"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/MINIMAL_BASIS_NEUTRAL_MACHINE_v0.4_FIXED.py",
        "sha": "e06b5bd42be1e6117a264d0b4799ef513d6f1495"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/MINIMAL_BASIS_SEARCH_D_R_W_P_v0.1.md",
        "sha": "f99f0c08a9af1431b49dbf31e80dd28d82856ca8"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/MINIMAL_BASIS_SEARCH_ENGINE_AUDIT_v0.2.md",
        "sha": "590645212a8ecc5996eecf053cb55480b3c50c85"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/MINIMAL_BASIS_SEARCH_ENGINE_AUDIT_v0.3.md",
        "sha": "b09efb4a39dca82da07f296b617bbb6c0b4c3359"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/MINIMAL_BASIS_SEARCH_ENGINE_v0.2.py",
        "sha": "661409cdc85841db7a8249ec362c74bc4ce281a2"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/MINIMAL_BASIS_SEARCH_ENGINE_v0.3.py",
        "sha": "bcde90280162baeb71e5ac92da4732fcba944e2a"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/MINIMAL_BASIS_SEARCH_ENGINE_v0.4.md",
        "sha": "751297c7597667aa5679f2aec4ad6828d067ce7f"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/MINIMAL_BASIS_SEARCH_EXECUTOR_AUDIT_v0.1.md",
        "sha": "3eff42acc676e0a0b718fe6cfddbccc14ef0fef4"
      },
      {
        "path": "03_EXPERIMENTS/FOUNDATION/MINIMAL_BASIS_SEARCH_EXECUTOR_v0.1.py",
        "sha": "55a31bdb538c6b005debdf639c31b42ad0fc5521"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RESEARCH_LOG.md",
        "sha": "3f2ed93742677c0e5dc18dc4b80cd53e1a42ec18"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-01_ATTACK_NOTES_2026-08-26.md",
        "sha": "e09ee4d5d28d15176eca5f65124cdf7e9f9d2bee"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-01_MATHEMATICAL_BASELINE.md",
        "sha": "12c67ab00f4e3f423b6738f854f9b68bf790f2fd"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-02_KERNEL_ATTACK_2026-08-26.md",
        "sha": "f896f7e7bcbdaebfecc490d6c19eac624717bcff"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-02_SECOND_LEVEL_CONCAVITY.md",
        "sha": "225bba6ac255413d764bb6c6453c825ddb0f59fb"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-03_JENSEN_HYPERBOLICITY_COMPUTATION.md",
        "sha": "60282a0476c8c48f5cf26147dd781315ed301b93"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-04_FINITE_STRIP_ATTACK_2026-08-26.md",
        "sha": "bd031fd9dd184a639a93cb447381f9552fd11aad"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-04_FULL_RUN_2026-08-26.md",
        "sha": "7fd1cf596b90506bd8f77a63f0c3ba9652a23081"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-05_FULL_RUN_AUDIT_2026-08-26.md",
        "sha": "6eec34523d0d7afcc4b4948e398e689482e9fa55"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-06_GERSHON_PROOF_AUDIT_2026-08-26.md",
        "sha": "89bbf6a521a60bcbe232f76d60b4cc291ffa6f8b"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-07_CIRCULARITY_AND_SPECTRAL_GAP_AUDIT_2026-08-26.md",
        "sha": "dfbf0634b7cce71b6aabaefc2617cbacbbc45b8e"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-07_GERSHON_LOAD_BEARING_GAP_2026-08-26.md",
        "sha": "cec8018986c27eab248ec0cb2f49efdfbba135e2"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-08_SPECTRAL_TAIL_AUDIT_2026-08-26.md",
        "sha": "1c910b1ed52c4c80a8cca84ef004eb63d4e49183"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-09_FULL_LINE_RESULT_2026-08-26.md",
        "sha": "807a93134166e82d17e3a289007da8f07f4c68e4"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-10_WEIL_INERTIA_FULL_LINE_2026-08-26.md",
        "sha": "5f2ec24680261fa9e93627ecc00d095977c1ce37"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-11_WEIL_GLOBAL_POSITIVITY_ATTACK_2026-08-26.md",
        "sha": "4ed12768df8e38a6c73203b085a26fb47a507cef"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-12_CANDIDATE_PROOFS_AUDIT_2026-08-26.md",
        "sha": "6ecca33747603bc576047cbb6039a067a7aee129"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-13_GLOBAL_CLOSURE_ATTACK_2026-08-26.md",
        "sha": "e9bf756f520be21fc596bf50b663640cdaf42cdb"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-14_CROSS_AUDIT_TOTAL_POSITIVITY_2026-08-26.md",
        "sha": "29dd04ef31be6e6b79aab2685ee49ff8a2782205"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-16_OPERATOR_LIMIT_ATTACK_2026-08-26.md",
        "sha": "b14caeb42072fece446054d085f824c6e98d81f6"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-17_FRIEDRICHS_SPECTRAL_AUDIT_2026-08-26.md",
        "sha": "f079cc1707f86e1094e2929a268a74212fc94165"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-18_GLOBAL_PROOF_AUDIT_2026-08-26.md",
        "sha": "4b0a7ae2acc50f30c643f0bafca8a23ad5b9cccc"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-19_FULL_RUN_VERDICT_2026-08-26.md",
        "sha": "c229b5472a2d0c83d5ed5f4d6cf6daecb5d3a604"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-20_UNIVERSAL_POSITIVITY_FINAL_ATTACK_2026-08-26.md",
        "sha": "91f7cc4409a4cfcd74a554ddeb64d597a3d68bd3"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-21_TWO_ROUTE_FULL_AUDIT_2026-08-26.md",
        "sha": "c576bb4d308ecfd7fb130700af3de1038aed90ef"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-22_VICERE_T3_AUDIT_AND_REPRODUCTION_PLAN_2026-08-26.md",
        "sha": "4a20f73d5c46be8222a8659069f7b7aaf3bd139d"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-23_FULL_RUN_VICERE_FORMULA_RESIDUAL_AUDIT_2026-08-26.md",
        "sha": "be274436be02e98b5475be84461fb27cb9191ac9"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-24_RESIDUAL_FORMULA_FULL_RUN_2026-08-26.md",
        "sha": "623a4082e9c559dc2e44a94a859652174fc8a534"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-25_MULTI_ROUTE_RUN_2026-08-26.md",
        "sha": "b55e7c9bcc18c799570f373aa599f718be501a9d"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-26_COMPOSITE_WEIL_HANKEL_VARIATIONAL_RUN_2026-08-26.md",
        "sha": "cdd31fb8964db94c145038e993e66501e147dba8"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-27_MULTI_ROUTE_SWEEP_2026-08-26.md",
        "sha": "4dfe2981530616c862c65bfcfa18231a6fa0f0d0"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-29_MULTI_ROUTE_DEEP_SWEEP_2026-08-26.md",
        "sha": "f1a91fd518c741764bd96205d2d56991a1b1e2b9"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-30_SICHE_KREIN_RUTMAN_AUDIT_2026-08-26.md",
        "sha": "a900d982be54770741684eb07fbcf39d7b6969a8"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-31_NONCOMPACT_SHIFT_PROOF_2026-08-26.md",
        "sha": "316081fc8780bd76a1fc963b8355e7220ec31fd0"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-32_COMPACT_RESOLVENT_REPLACEMENT_2026-08-26.md",
        "sha": "b87406c1ceea8bd8d2d97cdba41ef7bf96ebf10b"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-33_COMPACT_RESOLVENT_LEMMA_2026-08-26.md",
        "sha": "5d2dade89fec1c43102cc2e7621334355efa7678"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-34_FINITE_DICTIONARY_TO_LIMIT_BRIDGE_2026-08-26.md",
        "sha": "ca371786d64f970ee894bbd6de99c1b110e79c4f"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-34_RESOLVENT_POSITIVITY_SANITY_CHECK_2026-08-26.md",
        "sha": "1e291ca1715b85402c8c592f73a385b66844f8e3"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-35_LIMIT_BRIDGE_STATUS_2026-08-26.md",
        "sha": "eef48533b40b3e21ffecdbe1c6ca69692e3140f2"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-36_FORM_LIMIT_AND_NEGATIVE_WITNESS_2026-08-26.md",
        "sha": "3967d72631f16c3b50c64cb597ad75a4a99f75b0"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-37_FORM_CLOSURE_SWEEP_2026-08-26.md",
        "sha": "5580ac7aef3311f776e12d96e7c5ea164fb9c854"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-38_GALERKIN_TAIL_CLOSURE_2026-08-26.md",
        "sha": "bc1b35a87a3c5d8f6cb712ec1ac9b6218d7cdd30"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-39_DENSITY_CLOSURE_AND_TRUE_BOTTLENECK_2026-08-26.md",
        "sha": "19941a6ed68a61a2c6868ae32f49237fb4346b82"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-40_EXTERNAL_THEORY_SWEEP_2026-08-26.md",
        "sha": "4e130d6923fb2e7d84b74831765d8c20a91d32a5"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-41_THEORY_SWEEP_AND_ACCEPTANCE_GATE_2026-08-26.md",
        "sha": "a748e1a8f177bd25374bbabf4c57030152593c15"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-42_POLYA_KERNEL_AUDIT_2026-08-26.md",
        "sha": "a134d83a3103a637777c7013fc822bad8597ccae"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-43_PROOF_ACCEPTANCE_GATE_2026-08-26.md",
        "sha": "651331f0c02fabc9494a675e5a24ccb0205dae62"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-44_ROUTE_COMPETITION_2026-08-26.md",
        "sha": "47c83226bd7657ecf2fbb8cea730c156b1997466"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-45_SHIMIZU_ASSUMPTION_AUDIT_2026-08-26.md",
        "sha": "eeb13a5b3383cc25ac9c7a5ffca5e6142e540509"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-46_ANCHOR_PROTOCOL_2026-08-26.md",
        "sha": "cf038652f2609f3fcc3e279e5f065f6d74ca06d1"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-55_GLOBAL_LIMIT_AUDIT_2026-08-26.md",
        "sha": "2c8743b5331adba9c43deaaafa3974c54d4989fc"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-56_GLOBAL_LIMIT_REASSESSMENT_2026-08-26.md",
        "sha": "37d92580dddcdf42b1d4993b84770a0299e2e305"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-57_SHIMIZU_V8_AUDIT_2026-08-26.md",
        "sha": "0a0637e000be2684bfda2409db23ef350e188edf"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-58_G3_AUDIT_2026-08-26.md",
        "sha": "9019c2b0439b1e0077ba9a20ec62811eaa95a3aa"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-59_FULL_AUDIT_2026-08-26.md",
        "sha": "e99f449a8cc450b1b12c3b7a99c7da624ce4246a"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-60_FULL_CLOSURE_STATUS_2026-08-26.md",
        "sha": "371b09669827ae83559776d1cf0e0dec74c67b22"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-61_FINAL_AUDIT_2026-08-26.md",
        "sha": "fc7b35825bfb8d64114803fd734a471b7b4e7e11"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-62_TARGET_IDENTIFICATION_AUDIT_2026-08-26.md",
        "sha": "caacfb0cc0a11c060b3e253918104c29b6128af4"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-63_PRIMARY_SOURCE_AUDIT_2026-08-26.md",
        "sha": "e986be91c84c80ed594ec43d44a2e8204a50e16c"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/RH-64_SHIMIZU_FULLTEXT_AUDIT_2026-08-26.md",
        "sha": "663689c9f86416decdd2827e824fba0a9611f6eb"
      },
      {
        "path": "03_EXPERIMENTS/Omega-RH-01/noncompact_shift_sanity.py",
        "sha": "60b18f5626203673e43000c7f007b405c6ecc553"
      },
      {
        "path": "05_RESEARCH/RELATIONAL_PULSATION/REL-PULSE-01_AUTONOMOUS_RELATIONAL_OSCILLATION.md",
        "sha": "935159f3b40d78244bcf67508bd1dfc7b142e514"
      },
      {
        "path": "05_RESEARCH/RELATIONAL_PULSATION/REL-PULSE-02_CONSERVATION_FEEDBACK_SELECTION.md",
        "sha": "c935e0bb471973047689721f22ed6f346e8deec8"
      },
      {
        "path": "05_RESEARCH/RELATIONAL_PULSATION/REL-PULSE-03_SPATIAL_PROPAGATING_MODE.md",
        "sha": "464411b2ec5483c0a4738f2ec8d3acf14d34b532"
      },
      {
        "path": "05_RESEARCH/RELATIONAL_PULSATION/REL-PULSE-04_CURL_SELECTION_AUDIT.md",
        "sha": "c3a823f9976df2f3f9f2f0d4e775b95015418205"
      },
      {
        "path": "05_RESEARCH/RELATIONAL_PULSATION/REL-PULSE-04_CURL_SELECTION_AUDIT.py",
        "sha": "e137d05dbb10e48c73d1ea5df5932889e60355cb"
      },
      {
        "path": "EXPERIMENTS_ROOT/B0_initial_hypothesis.md",
        "sha": "e0525f5e927559fd5730404bc6bbc669606ca82a"
      },
      {
        "path": "EXPERIMENTS_ROOT/B1_internal_dynamics_vs_noise.md",
        "sha": "cc42c902a1b0c93e11b96b0d2156cc4f3ed1a22c"
      },
      {
        "path": "EXPERIMENTS_ROOT/B2_diffusion_rule_control.md",
        "sha": "3263d725281220451b27ad22749f08631b376b0c"
      },
      {
        "path": "EXPERIMENTS_ROOT/B3_null_model.md",
        "sha": "fb14f071211062421e6230a6c32d793106157ac6"
      },
      {
        "path": "EXPERIMENTS_ROOT/B4_fair_comparison.md",
        "sha": "6fcece5d88b123b523e544fcf5847b2b16e4fdea"
      },
      {
        "path": "EXPERIMENTS_ROOT/B5_spatial_shuffle.md",
        "sha": "49bb9015e857da841f5082791ba5681ee210dd10"
      },
      {
        "path": "EXPERIMENTS_ROOT/CICADA-3301/EXP-C1-002-FIBONACCI-GRID.md",
        "sha": "077cdefb681920f8827233134f9d197c2ba5a217"
      },
      {
        "path": "EXPERIMENTS_ROOT/CICADA-3301/EXP-C1-015-STATE-INVARIANT-AUDIT.md",
        "sha": "20860c828e0798c7574f7a37c54aac26326a121d"
      },
      {
        "path": "EXPERIMENTS_ROOT/CICADA-3301/EXP-C1-016-TOTIENT-MATRIX-GRAPH-CONTROL.md",
        "sha": "8aaaac0433eb2719ec084d11388b8776106279ab"
      },
      {
        "path": "EXPERIMENTS_ROOT/CICADA-3301/EXP-C1-017-MATRIX-TYPE-INVARIANTS.md",
        "sha": "92a43ef285a1daca7ad9e48e00bc7a2bf214128d"
      },
      {
        "path": "EXPERIMENTS_ROOT/CICADA-3301/EXP-C1-018-M3-FIBONACCI-SPIRAL-INVARIANT.md",
        "sha": "490850b8a3c814ae000b3cd3185502bae46916ca"
      },
      {
        "path": "EXPERIMENTS_ROOT/CICADA-3301/EXP-C1-019-M3-FIBONACCI-SPIRAL-CONTROL.md",
        "sha": "447f6241f9611c26b8767c97de1ae52898ec0870"
      },
      {
        "path": "EXPERIMENTS_ROOT/EMO/README.md",
        "sha": "d6d092f82ccbcfdb3e8171762cbb91a5879b3efb"
      },
      {
        "path": "EXPERIMENTS_ROOT/ENTITY_SEARCH/EXP_BIDIRECTIONAL_GOAL_V1_2026-09-17.md",
        "sha": "6a12866c69aaf40e4636b5f82694392f8abb4530"
      },
      {
        "path": "EXPERIMENTS_ROOT/ENTITY_SEARCH/EXP_PHYSICS_REVERSE_CONVERGENCE_V1_2026-09-17.md",
        "sha": "c7e739ba15fd1c7cf892c956bfd7482fbb5048e1"
      },
      {
        "path": "EXPERIMENTS_ROOT/ENTITY_SEARCH/EXP_PHYSICS_TO_OMEGA_BLIND_V1_2026-09-17.md",
        "sha": "bc3b2c26adb551a74f57f5b3865cb606f14f24a6"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/EXPERIMENT_HISTORY.md",
        "sha": "d278b10c189e091be017d7aa347f5696e7d8d07a"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/Omega-INF-1_character_order.py",
        "sha": "c2894646ee336da62a116f8c934b2a0ac7b35848"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/Omega-INF-2_hierarchical_permutation.py",
        "sha": "3d6ed9c76dce32787cf7eedb6779c87072f959ea"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/Omega-INF-2_hierarchical_scrambling.py",
        "sha": "d01164a4b7c5929bc0ba635b2609159d4fbc5cb8"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/Omega-INF-3_local_relations_preserved.py",
        "sha": "459c4aed037ae8c469109b5b918e22bdee3a118b"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/Omega-INF-4_local_relations_trigrams_preserved.py",
        "sha": "5dc59d49b57266c1a2929c974b7a2e5906170bd9"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/Omega-INF-5_independent_corpus_replication.py",
        "sha": "c1818ecf0f5460aae31801dbad960a8d6d1ce1db"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/Omega-INF-6_sampling_control.py",
        "sha": "34decc155597f918ac982496e9dc28946242a3ea"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/Omega-INF-7_robust_sampling.py",
        "sha": "8bc71e4eb18ecea19530f50fa0b3e3ccf73335b3"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/Omega-INF-8_break_it.py",
        "sha": "9831a8b034fb4a6d593c53e42b54676f6ed65989"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/README.md",
        "sha": "ca84ea4f2adc83386263e5b335d4079fde636c6a"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/README_Ω-INF-8.md",
        "sha": "f75ae0a818701476d089d0ba4c82e250be96b582"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/RESULTS-INF-2.json",
        "sha": "7143aa87eef6faa78901cc8a7f561a4ec04905a8"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/RESULTS.json",
        "sha": "aa8aac5825bf845937e1f3b7d1d4aaf26800749d"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/RESULTS_Omega-INF-2.md",
        "sha": "ba7c97b49ea44ba2ece0e84dcaf157dadccb6719"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/RESULTS_Omega-INF-3.md",
        "sha": "e43ed3563c24107bc324538fd96488e014e3df87"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/RESULTS_Omega-INF-4.json",
        "sha": "6e42f79d4a0a9a9d04b358c92a9da5bec624cc76"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/RESULTS_Omega-INF-4.md",
        "sha": "ef58b5e6efd3398701fec8dcc58cd6c24d3db8b9"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/RESULTS_Omega-INF-5.json",
        "sha": "82834b745de40450b62d997a292c36959afbb7a6"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/RESULTS_Omega-INF-6.json",
        "sha": "3b3a7923eb427b823e478cda952fbbd9f005ee49"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/RESULTS_Omega-INF-7.json",
        "sha": "f05302405d316feae4c91e75a0d4999b34828376"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/RESULTS_Omega-INF-8.md",
        "sha": "eb6170395179affc1b898475b90ab36f245bba26"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/TEST_REPORT_2026-08-13.md",
        "sha": "2b00e8ed876b69307aa26dcb0ae27fb24b27d30a"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/TEST_REPORT_2026-08-13_INF-2.md",
        "sha": "e6a8ef06a5d7b42ab664578b20f4715452af80eb"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/TEST_REPORT_2026-08-13_INF-3.md",
        "sha": "d0c250e10dae67010706481ae527da40fbee2d1f"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/TEST_REPORT_2026-08-13_INF-4.md",
        "sha": "62623b2532e56f2730de76a2d99433a323fd4035"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/TEST_REPORT_2026-08-13_INF-5.md",
        "sha": "62bc5f7a822ef5ef01c623d1a8142dc6db295fc1"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/TEST_REPORT_2026-08-13_INF-6.md",
        "sha": "8d940ab18a179f5f5201fca5462ebd54225e8eae"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/test_Omega-INF-1.py",
        "sha": "f7366553d1d43f6ee5faff9bea427d002bc279f5"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/test_Omega-INF-2.py",
        "sha": "fd8bd8c950177d55bbe1822d9587375077ed8650"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/test_Omega-INF-3.py",
        "sha": "49bb27ce099125d388795403952f639c0c5cb748"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/test_Omega-INF-4.py",
        "sha": "eb1458016616ad0c9aacaacd13d56f69f979e767"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/test_Omega-INF-5.py",
        "sha": "fe1d0e9b961123ca7630ae6a1f2d34de0cf59cd7"
      },
      {
        "path": "EXPERIMENTS_ROOT/INF/test_Omega-INF-7.py",
        "sha": "6ebcd3ca4a654acac9714f01f56da6ee3c3f2a2e"
      },
      {
        "path": "EXPERIMENTS_ROOT/MEM/Omega-MEM-1_abcd.md",
        "sha": "140b37056087178ccc8b5da5bcc762a91f05113f"
      },
      {
        "path": "EXPERIMENTS_ROOT/MEMORY/README.md",
        "sha": "6206e8e9a3596d8b9da304896c95b4c3063f5004"
      },
      {
        "path": "EXPERIMENTS_ROOT/O0_time_memory.md",
        "sha": "19a2e2136bd37a8fa7c1adf7e474efe355e08a48"
      },
      {
        "path": "EXPERIMENTS_ROOT/Omega-MEM-2.md",
        "sha": "3c5e6cd1dec6e6a17c0153e4cd4523dd90b91a8f"
      },
      {
        "path": "EXPERIMENTS_ROOT/Omega-SPEC-1_lightning_state_transition.md",
        "sha": "076397d033ededbade472ec804166071403a831c"
      },
      {
        "path": "EXPERIMENTS_ROOT/README.md",
        "sha": "abe126f83316102c6e7c615126416d642078d2e6"
      },
      {
        "path": "EXPERIMENTS_ROOT/Ω-MEM-2/STATUS_REVIEW.md",
        "sha": "a8cebb67d47a1d1d6b4986cdc56576b81654ce78"
      },
      {
        "path": "EXPERIMENTS_ROOT/Ω-MEM-TIME/PROTOCOL-Ω-MEM-3.md",
        "sha": "719987eaf952af362cb46796642a3453f319c7b0"
      },
      {
        "path": "RESEARCH_STATUS.md",
        "sha": "b7f1832192755ba5f30f65ed8a55fb69e3c0607a"
      },
      {
        "path": "experiments/REL-66_FUNCTIONAL_EQUIVALENCE_BLIND_PHYSICS.md",
        "sha": "782c3f61c1309d7081d341318370c2b254a15d1a"
      },
      {
        "path": "experiments/REL-67_FUNCTIONAL_EQUIVALENCE_PHYSICAL_AUDIT.md",
        "sha": "b521f7f08304b04c84811021d8b5239500974daf"
      },
      {
        "path": "experiments/REL-68_BLIND_TIME_SERIES_FINGERPRINT_PILOT.md",
        "sha": "5091238469aa0db718558fffe233e504e60ec3af"
      },
      {
        "path": "experiments/REL-69_BLIND_TIME_SERIES_FUNCTIONAL_CLUSTERING.md",
        "sha": "e5d2820c50f0e66883771dc1cc88b7e85851d326"
      },
      {
        "path": "experiments/REL-70_BLACK_BOX_DYNAMICS_FINGERPRINT.md",
        "sha": "fd22d6e7ceeda393e07ce961639c7b8ac8625237"
      },
      {
        "path": "experiments/REL-71_AUTOMATIC_DYNAMIC_FINGERPRINT_EXTRACTION.md",
        "sha": "fe58a38613fa21236a348cd374def51ffa07c9e8"
      },
      {
        "path": "experiments/REL-71_AUTOMATIC_DYNAMIC_FINGERPRINT_RESULT.md",
        "sha": "d7616c44a4ea743d8bd0e3082bdfb2155efdfd1a"
      },
      {
        "path": "experiments/REL-72_DELAY_VS_MEMORY_BLIND_TEST.md",
        "sha": "31009f0d27e311f5c5bd58aaca5c3c3f1dd38b33"
      },
      {
        "path": "experiments/REL-72_DELAY_VS_MEMORY_RESULT.md",
        "sha": "bd90f9a30e3163f37120c1db8be3869455701b71"
      },
      {
        "path": "experiments/REL-73_BLIND_UNSUPERVISED_BEHAVIOR_DISCOVERY.md",
        "sha": "1c3882921d0a9303bec675fa3615a4b07a853915"
      },
      {
        "path": "experiments_root/E-ENERGY-HYSTERESIS-BALANCE-001.md",
        "sha": "67c10966c10c00b0f67ae095b1cfcd4a8ac139ae"
      },
      {
        "path": "experiments_root/OMEGA-HYPOTHESIS/2026-08-13-STATE-FRAME-UPDATE.md",
        "sha": "57a1b67cd2acb910563e51a61f2d3c11fb045836"
      },
      {
        "path": "experiments_root/Omega-BASIS-002-R1/PROTOCOL.md",
        "sha": "f8ea068ebe4c1e9b3dded8a1bc62956c316b6094"
      },
      {
        "path": "experiments_root/Omega-BASIS-002-R2/AUDIT-2026-08-13.md",
        "sha": "74918959d0781b96c17ef6006eb3d29492b7206c"
      },
      {
        "path": "experiments_root/Omega-BASIS-002-R2/PROTOCOL.md",
        "sha": "440da75e0934c5485c255e5e77c71db6ea54858d"
      },
      {
        "path": "experiments_root/Omega-BASIS-002-R2/PROVENANCE_CLOSURE_v1.0.md",
        "sha": "744222f577f35006ee9e95f6a1c53b89c48f247f"
      },
      {
        "path": "experiments_root/Omega-BASIS-002-R2/RESULTS.md",
        "sha": "0a92cf2f2ae5a32b063e5db2e4131f18aad35668"
      },
      {
        "path": "experiments_root/Omega-BASIS-002-R2/run_r2.py",
        "sha": "cceea7ec016ef41eb34aea16fec997c14897c6ef"
      },
      {
        "path": "experiments_root/Omega-BASIS-002/FAILURE-2026-08-13.md",
        "sha": "f739377eccdf05fc1c566d51611a311f73807098"
      },
      {
        "path": "experiments_root/Omega-BASIS-002/PROTOCOL.md",
        "sha": "95bcb99a5f947982a927ec5f612d036a84720076"
      },
      {
        "path": "experiments_root/Omega-BASIS-002/run_state_time.py",
        "sha": "3100221c750e63cf5ad529d04e05d01f6a7b9080"
      },
      {
        "path": "experiments_root/Omega-CYCLE-1/README.md",
        "sha": "2313ce8e13e97833a7f58ad22589cdd89c201384"
      },
      {
        "path": "experiments_root/Omega-CYCLE-1/test_cycle.py",
        "sha": "3459fc167e0db34c27940db08964630a5a0074e6"
      },
      {
        "path": "experiments_root/Omega-EMO-001A-R1/PROTOCOL.md",
        "sha": "43320997e6f3867f505e04654d912504e824f4be"
      },
      {
        "path": "experiments_root/Omega-EMO-001A-R1/RESULTS.json",
        "sha": "ca4d75092cb45059bc6583f0d073a63eda6e65ef"
      },
      {
        "path": "experiments_root/Omega-EMO-001A-R1/RESULTS.md",
        "sha": "025cb0ec96012a2f974a79b1618edbb5973c4982"
      },
      {
        "path": "experiments_root/Omega-EMO-001A-R1/run_xyz_basis_control.py",
        "sha": "c8005d3bf81e5bf0ea9c8d899d2ff893803d9b3b"
      },
      {
        "path": "experiments_root/Omega-EMO-001A/FAILURE-2026-08-13.md",
        "sha": "292260b567b95a75cfd6ceb325f341c49590f419"
      },
      {
        "path": "experiments_root/Omega-EMO-001A/PROTOCOL.md",
        "sha": "51e72d44d76330b8f0ba720c188c52469ed0339e"
      },
      {
        "path": "experiments_root/Omega-EMO-001A/run_basis_control.py",
        "sha": "84b404e4263a00af1a3886c8c46a93ce55955c04"
      },
      {
        "path": "experiments_root/Omega-EXECUTION-1/README.md",
        "sha": "0e17125c0c204f3671e13cd86478afc83fe7a3e6"
      },
      {
        "path": "experiments_root/Omega-EXECUTION-1/execution.py",
        "sha": "2ea23d9f6250150b7afcdf9443b60e7117c9212f"
      },
      {
        "path": "experiments_root/Omega-EXECUTION-1/test_execution.py",
        "sha": "2f48d4b7da27b91ce188b355754646791de6a5a4"
      },
      {
        "path": "experiments_root/Omega-FEEDBACK-1/README.md",
        "sha": "bad86a1c58ee451a19b5c9f2f1c294937bad3a18"
      },
      {
        "path": "experiments_root/Omega-FEEDBACK-1/feedback.py",
        "sha": "6c499596c3463c5469b4834a7a44e86cbbcc3dbb"
      },
      {
        "path": "experiments_root/Omega-FEEDBACK-1/test_feedback.py",
        "sha": "6c8f977b9ab64852507df7347a45f1eddd4b4211"
      },
      {
        "path": "experiments_root/Omega-FUTURE-1/README.md",
        "sha": "89a1765a5a4665c50a2ecb8d9f8094eeaeba654d"
      },
      {
        "path": "experiments_root/Omega-FUTURE-1/future_orientation.py",
        "sha": "ec19c3a1824bd84cea42b497b897170301fa8773"
      },
      {
        "path": "experiments_root/Omega-FUTURE-1/test_future_orientation.py",
        "sha": "c66c89e7eb34616944bd6cc7a0bae1a2d12ce394"
      },
      {
        "path": "experiments_root/Omega-LINK-1/AUDIT_PRE_RUN.md",
        "sha": "fb763b676806a6cc324949f928874f196d65a518"
      },
      {
        "path": "experiments_root/Omega-LINK-1/LOCAL-GLOBAL-1.md",
        "sha": "6552ae7873788206134fc43fa2f21d5b044bffd3"
      },
      {
        "path": "experiments_root/Omega-LINK-1/README-INFLUENCE-1.md",
        "sha": "a6538ac24f13de843414bfd0d8c4e041041d20cd"
      },
      {
        "path": "experiments_root/Omega-LINK-1/README.md",
        "sha": "c357f502e0af16f166ec706306341dd1187d9342"
      },
      {
        "path": "experiments_root/Omega-LINK-1/RESULT-001.md",
        "sha": "932882e0f440129377b4037f30c1f6cbb261923c"
      },
      {
        "path": "experiments_root/Omega-LINK-1/RESULT-002.md",
        "sha": "b1af217ff855a733dd84145289d96a7e86c2e745"
      },
      {
        "path": "experiments_root/Omega-LINK-1/RESULT-003.md",
        "sha": "adca1682967b1f58125106cd724d6f28c3f8f7b0"
      },
      {
        "path": "experiments_root/Omega-LINK-1/RESULT-004.md",
        "sha": "ad27db7f34f27700426b8a321765323869b4a239"
      },
      {
        "path": "experiments_root/Omega-LINK-1/RESULT-005.md",
        "sha": "8e5fc1db0297698a5face12124c8ca0fde405d56"
      },
      {
        "path": "experiments_root/Omega-LINK-1/RESULT-006.md",
        "sha": "5a422e9e54f914739aae7ec64ce7259d8fe723f6"
      },
      {
        "path": "experiments_root/Omega-LINK-1/RESULT-007.md",
        "sha": "bbf48ccee59994e812b1a2b89357e544c459f0e8"
      },
      {
        "path": "experiments_root/Omega-LINK-1/RESULT-009.md",
        "sha": "256f75618b3382e4b47f17bd30f0d17e8dff17e4"
      },
      {
        "path": "experiments_root/Omega-LINK-1/RESULT-010-depth-sweep.md",
        "sha": "4dc3ee7737851b0452d682be2304ac496b4e21c0"
      },
      {
        "path": "experiments_root/Omega-LINK-1/RESULT-011-state-distinguishability-crosscheck.md",
        "sha": "cf96695445bced290f2389a0a283f68eaecf6df5"
      },
      {
        "path": "experiments_root/Omega-LINK-1/TRIGGER_RUN.md",
        "sha": "64ea223da1eff71fbfaf5361309767e41d93f9c5"
      },
      {
        "path": "experiments_root/Omega-LINK-1/addition_link1.py",
        "sha": "c92db9c428ddbe52e36f755c4f961f7642bb2358"
      },
      {
        "path": "experiments_root/Omega-LINK-1/corrected_hidden_explicit_control_link1.py",
        "sha": "70a95c415d39b515d40a9bafa86ea6955c50e7f3"
      },
      {
        "path": "experiments_root/Omega-LINK-1/deep_memory_link1.py",
        "sha": "ad030eb99c0220501587a38ed83c5939c9e978c8"
      },
      {
        "path": "experiments_root/Omega-LINK-1/depth_sweep_link1.py",
        "sha": "4448ae05343e8078aa1c6c817a1792cdf8ed12b8"
      },
      {
        "path": "experiments_root/Omega-LINK-1/direction_link1.py",
        "sha": "28e209888d624a6ce17b3d8773ec38b2dbd08dde"
      },
      {
        "path": "experiments_root/Omega-LINK-1/exhaustive_horizon_2memory_binary_link1.py",
        "sha": "24b2512022c676cea69bea1c64c9e9300a9c4251"
      },
      {
        "path": "experiments_root/Omega-LINK-1/exhaustive_horizon_3memory_binary_link1.py",
        "sha": "821bc3e340fdb5d0e9cc77259d508e416b62a716"
      },
      {
        "path": "experiments_root/Omega-LINK-1/exhaustive_horizon_3state_link1.py",
        "sha": "553c35ab04b20c0cdbad7c730a878a7f648eae67"
      },
      {
        "path": "experiments_root/Omega-LINK-1/exhaustive_horizon_link1.py",
        "sha": "ced2516ccc155f47d48c7d216b32df4466b32130"
      },
      {
        "path": "experiments_root/Omega-LINK-1/explicit_state_equivalence_link1.py",
        "sha": "5ec8b4b29dbc365f77ae9e7f0aaaa8e5ee29d5d5"
      },
      {
        "path": "experiments_root/Omega-LINK-1/future_divergence_link1.py",
        "sha": "15fd57a4591462a53306e425c5c4d8cd8b201569"
      },
      {
        "path": "experiments_root/Omega-LINK-1/hidden_history_link1.py",
        "sha": "f981a7669903ae10dac2f2e188d22f5621fb035a"
      },
      {
        "path": "experiments_root/Omega-LINK-1/horizon_mechanism_link1.py",
        "sha": "275029f886eddef714fa5e3cfeb2062b6b382d8f"
      },
      {
        "path": "experiments_root/Omega-LINK-1/influence_link1.py",
        "sha": "c7ff3fea5cd255f01b8f9c186ec1aa7c0381c794"
      },
      {
        "path": "experiments_root/Omega-LINK-1/local_global_link1.py",
        "sha": "41334ce68173ad981149d9ee53c81d2a65ee92ad"
      },
      {
        "path": "experiments_root/Omega-LINK-1/memory_state_link1.py",
        "sha": "8d984218f8563c98c1645ef7fecefc702cf906e9"
      },
      {
        "path": "experiments_root/Omega-LINK-1/minimal_horizon_link1.py",
        "sha": "12241027e39a55bc7d0c87c5712288d4864de5f1"
      },
      {
        "path": "experiments_root/Omega-LINK-1/minimal_state_link1.py",
        "sha": "03183d2f820d901e6043956464ffab5e4e918ed1"
      },
      {
        "path": "experiments_root/Omega-LINK-1/predictive_state_horizon_link1.py",
        "sha": "dba638ae5036f07c20a9e7db73971b3a2697becd"
      },
      {
        "path": "experiments_root/Omega-LINK-1/run_link1.py",
        "sha": "841efb97008bf2c3c1c49fceab7ac7633fb2275f"
      },
      {
        "path": "experiments_root/Omega-LINK-1/state_augmentation_link1.py",
        "sha": "be96f73de900dc8cadf962ba6ec2f071385b7178"
      },
      {
        "path": "experiments_root/Omega-LINK-1/state_distinguishability_link1.py",
        "sha": "bdbca18c86e0d4bf0515fdfbd6ffb5e96709d858"
      },
      {
        "path": "experiments_root/Omega-LINK-1/state_distinguishability_v2_link1.py",
        "sha": "94853ee4267d281986c65d6711c442fec71b3031"
      },
      {
        "path": "experiments_root/Omega-MEM-1a-d/README.md",
        "sha": "450a0e4c0d6101290fafb623a12f99a5f865db06"
      },
      {
        "path": "experiments_root/Omega-MEM-1a-d/omega_mem1a.py",
        "sha": "f4d441dcfaa0cdfccd01dea0aa2b07599c42ba7a"
      },
      {
        "path": "experiments_root/Omega-MEM-1a-d/omega_mem1b_1c_1d.py",
        "sha": "d58ba094e676a540246b7f92d8e512db497fe190"
      },
      {
        "path": "experiments_root/Omega-MEM-2/README.md",
        "sha": "f662a5f103b48a905b1959527b7ebe7965e9b844"
      },
      {
        "path": "experiments_root/Omega-MEM-2/omega_mem2.py",
        "sha": "f341aa896ae86cb90772093ddb79224ae5d5d0ad"
      },
      {
        "path": "experiments_root/Omega-MEM-3/README.md",
        "sha": "5d5c8bdc501e01a6d13a9b74f213263c48f27857"
      },
      {
        "path": "experiments_root/Omega-MEM-3/omega_mem3.py",
        "sha": "88e2fb6b31237c8d027747054147ae1abd8d871c"
      },
      {
        "path": "experiments_root/Omega-MEM-4/AUDIT_MEM4_2026-08-10.md",
        "sha": "b6dbe0099c8d7274966b45184722e60aab8430ec"
      },
      {
        "path": "experiments_root/Omega-MEM-4/PROTOCOL.md",
        "sha": "df06783f128ac462b37775a4a198f03bd11c090d"
      },
      {
        "path": "experiments_root/Omega-MEM-4/README.md",
        "sha": "fc8f9f81dab93d26c0f3ecfec4707d34749ea2ce"
      },
      {
        "path": "experiments_root/Omega-MEM-4/omega_mem4_as_reported.json",
        "sha": "6ed4ccbe67a6111bf6ef76de670ab938396b08ce"
      },
      {
        "path": "experiments_root/Omega-MEM-4/omega_mem4_submitted.py",
        "sha": "6ff32312a37c8b5498778ab8107edf6d0e137167"
      },
      {
        "path": "experiments_root/Omega-MEM-4R/PROTOCOL.md",
        "sha": "306cc5e9a6547a8c47a876828dfd36c27a37f045"
      },
      {
        "path": "experiments_root/Omega-MEM-4R/README.md",
        "sha": "ad70d7538564d2fdb63affe2d4f4e245f5054e9d"
      },
      {
        "path": "experiments_root/Omega-MEM-4R/RESULTS.md",
        "sha": "bfbd82da0347e9cd544e0ab844032eb7ffbc4cac"
      },
      {
        "path": "experiments_root/Omega-MEM-5/AUDIT.md",
        "sha": "e87baafc2e3327827a5e4a774a7d7314a95775b4"
      },
      {
        "path": "experiments_root/Omega-MEM-5/PROTOCOL.md",
        "sha": "02a16909291402f5573c226f428ee313ef5582e0"
      },
      {
        "path": "experiments_root/Omega-MEM-5/README.md",
        "sha": "095ea4c380b5fd31c16859b8d002695d9daad735"
      },
      {
        "path": "experiments_root/Omega-MEM-5/RESULTS.md",
        "sha": "e724702ccfcbae0e95227d1f7641d6b8fe6d9174"
      },
      {
        "path": "experiments_root/Omega-MEM-5/run_mem5.py",
        "sha": "d5923718317313eec0e25a73d023213f43598c4d"
      },
      {
        "path": "experiments_root/Omega-MEM-6/AUDIT_PILOT.md",
        "sha": "523b56caa9e96c10907cdaccbe2d886786a05348"
      },
      {
        "path": "experiments_root/Omega-MEM-6/FULL_RUN_2026-08-14.md",
        "sha": "f20897e878b59871e75d881df44dee42fcfd0180"
      },
      {
        "path": "experiments_root/Omega-MEM-6/README.md",
        "sha": "60f2975d39a35b3a9a067473e316e419c58b2452"
      },
      {
        "path": "experiments_root/Omega-MEM-6/RESULTS_PILOT.md",
        "sha": "ee678295f4f0eda581d9bc16ce148e5d045c65be"
      },
      {
        "path": "experiments_root/Omega-MEM-6/run_mem6_pilot.py",
        "sha": "fe252d0b17fff6a03ebf1a5229e92c9362f594c2"
      },
      {
        "path": "experiments_root/Omega-MEM-7/AUDIT_PRELIMINARY.md",
        "sha": "9de6db37566a9fc00a259abd7f92535d0b4485df"
      },
      {
        "path": "experiments_root/Omega-MEM-7/README.md",
        "sha": "79d40af436fa7b9bdac3578951ecba73d0b67013"
      },
      {
        "path": "experiments_root/Omega-MEM-7/RESULTS_PRELIMINARY.md",
        "sha": "d903fa2c7419dcb2eea2e75c6bf57a143638ceae"
      },
      {
        "path": "experiments_root/Omega-MEM-7/run_mem7.py",
        "sha": "f7e3e9b6f4d4868d43332b6065289c05a7e016d7"
      },
      {
        "path": "experiments_root/Omega-MEM-8/AUDIT_PILOT.md",
        "sha": "ca3293d8a22c7db780d4c01c528b503be96e2c7d"
      },
      {
        "path": "experiments_root/Omega-MEM-8/README.md",
        "sha": "2408319749f1d69844f3818e5ec42f0d77995921"
      },
      {
        "path": "experiments_root/Omega-MEM-8/RESULTS_PILOT.md",
        "sha": "d9948bbc39dc42fcbc3a9b06ef7fb74305eaa686"
      },
      {
        "path": "experiments_root/Omega-MEM-8/run_mem8.py",
        "sha": "872ccce88e1679f4a6d5db8f9ef231c9fd8217cb"
      },
      {
        "path": "experiments_root/Omega-MEM-9/AUDIT_DYNAMICS_PRE_RUN.md",
        "sha": "8db1d40034e49f5abed14b27efd75656062109c1"
      },
      {
        "path": "experiments_root/Omega-MEM-9/AUDIT_GRAPH_PRE_RUN.md",
        "sha": "b01cd61d683ae122f0875da07184ac95ca345eca"
      },
      {
        "path": "experiments_root/Omega-MEM-9/AUDIT_PRE_RUN.md",
        "sha": "d0a15b885dc3faa527fc9784eecd29f0cfe7262e"
      },
      {
        "path": "experiments_root/Omega-MEM-9/README.md",
        "sha": "f6f6bc9406a705accd2ff6f238878a8d311e2f8d"
      },
      {
        "path": "experiments_root/Omega-MEM-9/run_mem9.py",
        "sha": "04ab56bf7740e8241e0b67fd315401caf82bfd57"
      },
      {
        "path": "experiments_root/Omega-MEM-9/run_mem9_dynamics.py",
        "sha": "fe4e1fd693554ff3ddc9f8cd94681a6a2bb263b8"
      },
      {
        "path": "experiments_root/Omega-MEM-9/run_mem9_graph.py",
        "sha": "39616ba4eac44dd8d907fe38735fd4ce7c177c20"
      },
      {
        "path": "experiments_root/Omega-PLAN-1/INTEGRATION_TEST.md",
        "sha": "55efc83dedbba5db055002ece86587b690538721"
      },
      {
        "path": "experiments_root/Omega-PLAN-1/README.md",
        "sha": "6c6e47d1f3a30cba3306bf812c82e04b6921deae"
      },
      {
        "path": "experiments_root/Omega-PLAN-1/plan.py",
        "sha": "af7255bd94af3965f7c461ea5a48776f880826c3"
      },
      {
        "path": "experiments_root/Omega-PLAN-1/plan.schema.json",
        "sha": "04f6676cba451989eb975b08e398b024db141b8f"
      },
      {
        "path": "experiments_root/Omega-PLAN-1/test_plan.py",
        "sha": "f9d9bb1c84ec5dc06cb88560d51fc03210d6466e"
      },
      {
        "path": "experiments_root/Omega-PRESENT-1/IMPLEMENTATION_STATUS.md",
        "sha": "98e3164cab64ad91fb3d13d4ab4011c22cf57e2d"
      },
      {
        "path": "experiments_root/Omega-PRESENT-1/README.md",
        "sha": "6d039f3701f0b5689ee7d4fc6a3fc38dfb9530b4"
      },
      {
        "path": "experiments_root/Omega-PRESENT-1/current_state.py",
        "sha": "4fa97a7f7521ff33aa012ea67f8be88fe170790e"
      },
      {
        "path": "experiments_root/Omega-PRESENT-1/current_state.schema.json",
        "sha": "1ab74d4007e36f3c597fa28c458e24b345e84b1b"
      },
      {
        "path": "experiments_root/Omega-PRESENT-1/memory_present_link.py",
        "sha": "4c6e9c10ae91834387193366ca39d04418d26ddb"
      },
      {
        "path": "experiments_root/Omega-PRESENT-1/test_current_state.py",
        "sha": "9cd419aa493a7bd60ca1e1b6570b7d8599179ca2"
      },
      {
        "path": "experiments_root/Omega-VERIFICATION-1/README.md",
        "sha": "a459dd8e3e76caa3ef4e16b6af1802b1025420d2"
      },
      {
        "path": "experiments_root/Omega-VERIFICATION-1/test_verification.py",
        "sha": "30bc90b4e4f9611076b6f12f513000f62f331bd4"
      },
      {
        "path": "experiments_root/Omega-VERIFICATION-1/verification.py",
        "sha": "d821935aae26db4f02ffcbe416a516e5ad2fc467"
      },
      {
        "path": "experiments_root/code/e_energy_preisach_hysteresis.py",
        "sha": "abac87c10410b4d63c19025a38f93157e7c336ac"
      },
      {
        "path": "experiments_root/energy_hysteresis_balance_001.py",
        "sha": "d44ebd2d2d6d19013722666ac30772f6af7cc4af"
      },
      {
        "path": "experiments_root/results/E-ENERGY-PREISACH-001.md",
        "sha": "1cf80a159b1f43eb54475001d7cf696c964cb854"
      },
      {
        "path": "market/experiments/EXP-0009-data-driven-state-discovery.md",
        "sha": "d00b6860cf7ac89d9edac1a2cefff6678b36926a"
      },
      {
        "path": "market/experiments/EXP-0010-k-state-sweep.md",
        "sha": "f2db1b10338aeca1bd3779ec73bfb603ea6ebb32"
      },
      {
        "path": "market/experiments/EXP-0011-OI-price-divergence.md",
        "sha": "bbbfb86349a75fe6bbc75585433fc37f527a833d"
      },
      {
        "path": "research/ARCHIVE/2026-08-13-OMEGA-FULL-CHAT-AUDIT.md",
        "sha": "2307fafa9404b585b59b805f870bfe48ec150993"
      },
      {
        "path": "research/ENERGY/ENERGY_DUAL_MODE.md",
        "sha": "f85358af76aec07f54125de212f36b314ecc5851"
      },
      {
        "path": "research/ENERGY/README.md",
        "sha": "e9edd4f7db55cdcc09a8e5c78cf9ab7f15cc3eb7"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0010.md",
        "sha": "3498f7661677af09890c461291d38e486200c737"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0011.md",
        "sha": "93c4cdd8538b7af8b6b6c85ebd7cc9dd72e4f319"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0012.md",
        "sha": "39987d1cd2b63cfa233d72b86417adc10d946a3e"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0013.md",
        "sha": "6ff5ea2beaaac6001c59093c89a047b0772528ac"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0020.md",
        "sha": "6748c59e5c54c8ef8957f4017e789846318d64f0"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0021.md",
        "sha": "d7e15622f1613436206d6773ec05ae0c3f5f9cf4"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0022.md",
        "sha": "1c7184f9787c6eddfe498fa73e072131c2d96db2"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0023.md",
        "sha": "ba1854d9b5fa4ac2157113996837394b885f9903"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0024.md",
        "sha": "147cb78165aadfaf3b0db2da8cb5b36da977b473"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0025.md",
        "sha": "a1bf0f73cd046fe6c462797ce9c8d8b8bd3b202a"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0026.md",
        "sha": "9ecaaf75a1ea1b96c8939af87f1bb50f8ba39183"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0027.md",
        "sha": "443f83bf8b4130a1584166449d9a14d894e256ab"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0028.md",
        "sha": "ed14107910a69e897e000ac646a2526c8f6f777d"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0029.md",
        "sha": "219ebd977e4371f785feb80e28b0f78a8dc7f28c"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0030.md",
        "sha": "c0dfba646faa9a8c64c151f178a8d08628737abf"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0031.md",
        "sha": "7ecdab90bb605f92de1ff23e17de79708d41ee67"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0032.md",
        "sha": "0d8eed196dd23cb43491da73e4d82d4a818a6b88"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0032R.md",
        "sha": "eba39555e0fc03f3e05f1385b538014c66c54769"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0033.md",
        "sha": "70dd75dde392d15f6bfe4240ff6ca27f1a7c1889"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0034.md",
        "sha": "65a1e64c5ede1aeb9ef03e6bf53652ead7783eae"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0035.md",
        "sha": "0fb9c511820cb93fbe98925d809bac2df92609e2"
      },
      {
        "path": "research/ENERGY/experiments/E-ENERGY-0036.md",
        "sha": "6ceb219a89e48897e25f645e99018d3551dd82f3"
      },
      {
        "path": "research/RELATIONS/EDGE-PROPERTIES.md",
        "sha": "2d7ffaf5a049fca1680668476c7b3fe091b84368"
      },
      {
        "path": "research/RELATIONS/OMEGA-REL-001-INDEPENDENT-RELATION-COMPONENTS.md",
        "sha": "a7dfebe4143e720e35e4aa60fb865b0300961a08"
      },
      {
        "path": "research/RELATIONS/OMEGA_R_ANCHOR.md",
        "sha": "fd871db8de992f6950d26547b546f83a51d03382"
      },
      {
        "path": "research/RELATIONS/README.md",
        "sha": "905e76ef10f7971d26978848be0f97b209ad1996"
      },
      {
        "path": "research/RELATIONS/RELATION-COLLAPSE-ATTRACTOR-HYPOTHESIS-2026-08-13.md",
        "sha": "80c45366035627bee929821ddd214b1dcb62581b"
      },
      {
        "path": "research/RELATIONS/RELATION-CONFLICT-MEMORY-2026-08-13.md",
        "sha": "82143ce98feed92ff6826c923799b7cc554513b2"
      },
      {
        "path": "research/RELATIONS/RELATION-DUALITY-2026-08-13.md",
        "sha": "e863522fc0c881f1249b3a832f8dbc5a6b8e1fc7"
      },
      {
        "path": "research/RELATIONS/STRUCTURE-AND-PROPAGATION.md",
        "sha": "5d41ce950b435ac8c110d16fad60e42a0aa117bb"
      },
      {
        "path": "research/RELATIONS/archives/OMEGA-RELATIONS-EXPERIMENTS-037-046-SUMMARY.md",
        "sha": "a8263fdf453b2b77f10e0e66dbdc5238429283d8"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-MEDIUM-001-EMERGENT-LOCALIZED-STRUCTURES.md",
        "sha": "8925287ff2bc104aa947f07cbe5d952fedd3744c"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-MEDIUM-001-EMERGENT-LOCALIZED-STRUCTURES.py",
        "sha": "0c457b59fb58c9300089edafee9cc91332816535"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-MEDIUM-002-ELECTRON-HUNT.md",
        "sha": "095ee5c0241b6fd3d60ddb9e43f0f1828c2e0f80"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-PHYS-CROSSCHECK-001.md",
        "sha": "4a7ea273c645e93ed19c9a22c5870fc2fa19fc18"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-PHYS-ELECTRON-002.md",
        "sha": "ac8ffb31edcf4566630068bc8cb0cf474b401310"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-PHYS-ELECTRON-002A-VERIFICATION.md",
        "sha": "ffe071365ab7f346408d901344bbd7d875257f81"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-PHYS-ELECTRON-003-BLIND-RELATION-CLUSTERING.md",
        "sha": "bf111e2a1d528cfa4ee1d9b7bf43d22ba532790e"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-PHYS-ELECTRON-004-BLINDED-HELDOUT-RELATIONS.md",
        "sha": "ca594b7f0064543f802d3ecfb323ffa9b9da4760"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-PHYS-ELECTRON-004-BLINDED-HELDOUT-RELATIONS.py",
        "sha": "955ce8f172b8ddf0e0fb0ff2771bd8f45439ed82"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-PHYS-ELECTRON-005-HELDOUT-PROCESS-PREDICTION.md",
        "sha": "3b366cf002305c3f32b84f12dce158562609a559"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-PHYS-ELECTRON-005-RESULT.md",
        "sha": "d488d5018320a75807bc201888e76878131cef54"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-001-INDEPENDENT-RELATION-COMPONENTS.py",
        "sha": "3676b7a4f55eb9c1bbd8fc0bf496626e3c7dc7c5"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-002-WEIGHTED-RELATIONS.py",
        "sha": "c61466ab94fe2e4b609d134375d51876444bf427"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-002A-OBSERVATIONAL-SUFFICIENCY.md",
        "sha": "5fa5aa596ef8d7d7068bcb9371e92e20892590de"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-003-NO-DECAY.md",
        "sha": "76f88bc99bbbe8a0d67d21baa5a85d3ec6b889c0"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-004A-CAUSAL-PERSISTENCE.md",
        "sha": "e8405a248a2b01248a4126db14871cc0fbca82e7"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-004B-MARKOV-SUFFICIENCY.md",
        "sha": "56d97364bbab5f17ac514916a981f08961ec3b9b"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-005-006-TWO-STEP-INTERACTION.md",
        "sha": "6e15d99064d171e8cb8193c99335cc1b743b0a91"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-007-COMPARISON.md",
        "sha": "cd32504dfbc8bbe3fa585c4b5076c3d8b4f9066e"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-007-STABLE-RELATION-CLASSES.md",
        "sha": "f49dbfede6a7fa33776dc483deb558f817e87f13"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-009-CONFLICT-MEMORY.py",
        "sha": "40986ea3720717c8ab4d23227ccc0b7e88ca39ed"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-009-RESULTS.md",
        "sha": "967fd44926171cd73af5ce27aeab80b414e73aed"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-010-CONTROLLED-MEMORY-RESULTS.md",
        "sha": "2d15a7d1968b21585a1d6efbe2b06f35f6f90d65"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-010-SELF-GENERATING-RELATION-SPACE.md",
        "sha": "fd1a37a1529fef1315e3d716471ac1d6274f3b3a"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-011-012-MEMORY-AS-BOUNDARY.md",
        "sha": "1c5dca2b120628aec451802eb4ac47f69c0cf4d6"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-012-MEMORY-AS-BOUNDARY.py",
        "sha": "37cb16e126e9a1fd7badfaf1889a3d57125764a6"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-016-BOUNDARY-FEEDBACK.md",
        "sha": "7ec0b7e528093cd1360ff98033558c9c1da65b21"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-018-SURGICAL-MEMORY-DELETION.md",
        "sha": "0efdae8f89c15d59817f20c6ced79ad6b8b1afe6"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-024-INVARIANCE-STRUCTURAL-CLASSES.md",
        "sha": "47831ed36a3d0f5deb5ed7d23cf682704308202c"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-029-SAME-RELATION-DIFFERENT-FUTURE.md",
        "sha": "b4f5a1fadbb9229cfca23f461faf804dfed406d5"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-036-FOUR-STATE-DYNAMICS.md",
        "sha": "8161787c540e0aa5b6b2b04a627ef7cd7a270165"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-041-GENERATOR-INDEPENDENCE.md",
        "sha": "8a495558b6a745a0f45fd4ecec8ca229ec5cfd2f"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-043-REVERSIBLE-OPERATIONS.md",
        "sha": "28e735b704359c469afbed54d7aaa8549d01caef"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-REL-045-DERIVED-DISTANCE.md",
        "sha": "61690263801576232687ec857cbf05d924b01c3c"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-STRUCTURE-001-RULE-PRESERVATION-THROUGH-DECAY-2026-08-30.md",
        "sha": "b52da49fa543c7b8b704e9857d2f95d13a90134c"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-001-DISTINCTION-ORDER-DURATION-2026-08-27.md",
        "sha": "e480222cbf9e76a6938feb5a3cd4a601940e07bf"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-001-DISTINCTION-ORDER-DURATION-2026-08-27.py",
        "sha": "40bef3a2ff0f2d7b2d23e9fc6b42529a1a82c924"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-002-RELATIONAL-TEMPORAL-COORDINATE-2026-08-27.md",
        "sha": "8c568481c1be3a669bba6a89fe6be8d843ee8210"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-002-RELATIONAL-TEMPORAL-COORDINATE-2026-08-27.py",
        "sha": "1d8d649703c81483ce93d34033f4028a03e9349e"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-003-005-FULL-TEMPORAL-LIFE-CYCLE-2026-08-27.md",
        "sha": "51311fd60f1ff59236f05615e47737f080551d72"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-003-005-FULL-TEMPORAL-LIFE-CYCLE-2026-08-27.py",
        "sha": "edd7a7261e9d1b49637381ab1b527d53cfd19cb2"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-006-DYNAMIC-METRIC-BOUNDARY-2026-08-27.md",
        "sha": "1c65f15f66a319cd28d3b4502450758a55a7542d"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-006-DYNAMIC-METRIC-BOUNDARY-2026-08-27.py",
        "sha": "a3f7b9c37e0532e2d884f0a2b534760e7e406c30"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-007-FREQUENCY-SPEED-TIME-2026-08-27.md",
        "sha": "233cc916ddaa754e4d99d014e5c403841526ed35"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-007-FREQUENCY-SPEED-TIME-2026-08-27.py",
        "sha": "5e931c5e2218e1340d17fa4c2176790301484b85"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-008-INDEPENDENT-CLOCKLESS-SYNCHRONIZATION-2026-08-27.md",
        "sha": "521d88b5f4bea026452ec2bb4580101baa33ffe3"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-008-INDEPENDENT-CLOCKLESS-SYNCHRONIZATION-2026-08-27.py",
        "sha": "e0214604db95b97a3c5d49465b7b98bf449aac01"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-009-INTERNAL-SCALE-BOUNDARY-2026-08-27.md",
        "sha": "fd6bfcd98119126b1d2f9ed23c1e4876afbf23f0"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-009-INTERNAL-SCALE-BOUNDARY-2026-08-27.py",
        "sha": "ad74064a15b7b5ec52191d93c7273dc3ae53d3cd"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-010-FLOW-STATES-2026-08-27.md",
        "sha": "b3bd8b1924f2a89a608936fc75604a4ea49ab87e"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-010-FLOW-STATES-2026-08-27.py",
        "sha": "64e865b217721ca649f4001b159a03322b76f611"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-010-RESULTS-2026-08-27.md",
        "sha": "af0820a0b4f4fe200e7c4d368d9eb4a54ec720ad"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-011-TEMPORAL-MEDIUM-BOUNDARY-2026-08-27.md",
        "sha": "4352ea9b0a78385f29f856009c05929d25501f21"
      },
      {
        "path": "research/RELATIONS/experiments/OMEGA-TIME-011-TEMPORAL-MEDIUM-BOUNDARY-2026-08-27.py",
        "sha": "ab6495331644701d22d69c713e45f5f3580c3baa"
      },
      {
        "path": "tools/graph_memory_inspector/test_inspector.py",
        "sha": "d5e2ca8552acad4a4ac106dfcd6fb75022daf0de"
      }
    ],
    "ORISIK": [
      {
        "path": "03_ARCHIVE/RESEARCH_ARCHIVE_RULES.md",
        "sha": "3b886a2ecd7541a713609391dbb768c21d37d68e"
      },
      {
        "path": "04_EXPERIMENTS/AUDIT/README.md",
        "sha": "2581bb1b0454c097d27cbb65743d2e8e447f15dc"
      },
      {
        "path": "04_EXPERIMENTS/EXECUTION/README.md",
        "sha": "8f3334e35f62051c5f8e4e5ac753ee7bc8750ae4"
      },
      {
        "path": "04_EXPERIMENTS/EXPERIMENT_REGISTRY.md",
        "sha": "0b30c738a9aa4f7bc4ae47b00542ff4edd60200a"
      },
      {
        "path": "04_EXPERIMENTS/FEEDBACK/README.md",
        "sha": "6aae3facd335adf0b23f1792caf2b56265292867"
      },
      {
        "path": "04_EXPERIMENTS/GRAPH/CL-SCALING-001.md",
        "sha": "aff89ff5e13e7fdd8c412e2a90aba6b58cd8ea02"
      },
      {
        "path": "04_EXPERIMENTS/GRAPH/CL-SCALING-001_EXECUTION_2026-08-19.md",
        "sha": "fd5eeb8a847deaf169ecd5ba66a7e6208d28e3b5"
      },
      {
        "path": "04_EXPERIMENTS/GRAPH/CL-SCALING-001_LOCAL_RESULT_2026-08-19.md",
        "sha": "47d54a3cc230c81fb3c8bc27fab4df508b014e44"
      },
      {
        "path": "04_EXPERIMENTS/GRAPH/CL-SCALING-001_PARALLEL_RESULT_2026-08-19.md",
        "sha": "41152172b0f047b618d87373472fae27c3516ca4"
      },
      {
        "path": "04_EXPERIMENTS/GRAPH/CL-SCALING-001_PARTITION_RESULT_2026-08-19.md",
        "sha": "d8bcf2a5fbe19cbfc49b46b2c34550a70c4b4faf"
      },
      {
        "path": "04_EXPERIMENTS/GRAPH/CL-SCALING-001_PROTOCOL_v1.1.md",
        "sha": "af9969c258eb3ba6d40c67cb7c46310296a74e6f"
      },
      {
        "path": "04_EXPERIMENTS/GRAPH/CL-SCALING-002_CONNECTION_AUDIT_2026-08-21.md",
        "sha": "b41adbd2d0bb9b6d073b017ab5b6308313250b9d"
      },
      {
        "path": "04_EXPERIMENTS/GRAPH/CL-SCALING-002_LOCAL_REPRODUCTION_2026-08-22.md",
        "sha": "6f9610ec0f603c6537de51d153e8ee02bc3076bc"
      },
      {
        "path": "04_EXPERIMENTS/GRAPH/CL-SCALING-002_PLAN_v1.0.md",
        "sha": "d5ba4a5426685ed351b4b544dd2ad79ebbe956d7"
      },
      {
        "path": "04_EXPERIMENTS/GRAPH/CL-SCALING-002_PROCESS_WORKERS_PROTOCOL_v0.1.md",
        "sha": "bdced76bf9db7a753b39ec937b353f8c4d59207f"
      },
      {
        "path": "04_EXPERIMENTS/GRAPH/CL_CONNECTION_AUDIT_v0.1.md",
        "sha": "a0bea0d2075d01cef0e5115d2cda4009973fa185"
      },
      {
        "path": "04_EXPERIMENTS/GRAPH/README.md",
        "sha": "035e507dbe5a988ff6539a9b35533ddb33b9bbf8"
      },
      {
        "path": "04_EXPERIMENTS/GST_COOLING_HISTORY_RELATIONAL_RESULT_v0.1.md",
        "sha": "e70ec82e6ef7d1bb99df4130511d67a707007817"
      },
      {
        "path": "04_EXPERIMENTS/GUARDIAN/README.md",
        "sha": "ed381fb88ad21b0f66477470fcae5ff185317f45"
      },
      {
        "path": "04_EXPERIMENTS/LAB/README.md",
        "sha": "721c320538c28b7c9fc969df14ed13f1f31bf961"
      },
      {
        "path": "04_EXPERIMENTS/LIGHT_COLOR_ENTROPY_BENCHMARK_v0.1.md",
        "sha": "5628234ce1d0d3fb7a7fe878003405429445f46e"
      },
      {
        "path": "04_EXPERIMENTS/LIGHT_INFORMATION_RELATIONAL_ENCODING_v0.1.md",
        "sha": "a095f6793ce4f82db9fbc80de727f6cb9478b15f"
      },
      {
        "path": "04_EXPERIMENTS/MEMORY/README.md",
        "sha": "7e11274258d6e26033bd18a65677561df0cf7d90"
      },
      {
        "path": "04_EXPERIMENTS/ORISIK_TIME_METRIC_BENCHMARK_v0.1.md",
        "sha": "3403d1fa9810d70f2dd663fcf59c689d7a08374e"
      },
      {
        "path": "04_EXPERIMENTS/PERCEPTION/README.md",
        "sha": "b9bfcf4ee6a55bece342b385872fe77376e858fc"
      },
      {
        "path": "04_EXPERIMENTS/PHYSICALIZED_RELATION_MEMORY_PHASEFIELD_v0.1.md",
        "sha": "f428ff780eb13676df6c6bd8f4dfef4981374ae5"
      },
      {
        "path": "04_EXPERIMENTS/PHYSICAL_PCM_RELATIONAL_MEMORY_v0.1.md",
        "sha": "a6317bf260812e91dedf7111bfff1f33f0b9a50e"
      },
      {
        "path": "04_EXPERIMENTS/PLANNING/README.md",
        "sha": "e16f2ad3611b2ea574989b2d615bef18c88ecde5"
      },
      {
        "path": "04_EXPERIMENTS/README.md",
        "sha": "6136c1739d46bd311520906b09ff8f82e5b723e6"
      },
      {
        "path": "04_EXPERIMENTS/REASONING/README.md",
        "sha": "92018202bbe78ce12cc597d93b7a309db56d6e4e"
      },
      {
        "path": "04_EXPERIMENTS/RECOVERY/README.md",
        "sha": "5754091f65119b4d085bb5e68cceb805ee7e6904"
      },
      {
        "path": "04_EXPERIMENTS/RECOVERY/SOURCE/EXP-0013_MEMORY_RECONSTRUCTION.md",
        "sha": "9b6a391472785525e78f723e71d7c9c793a8365a"
      },
      {
        "path": "04_EXPERIMENTS/RECOVERY/SOURCE/EXP-0014_RECOVERY_VALIDATION.md",
        "sha": "d868a7d454060c79c2538a0391ab4e88fcf46687"
      },
      {
        "path": "04_EXPERIMENTS/RECOVERY/SOURCE/EXP-0015_RECOVERY_DAMAGE_SWEEP.md",
        "sha": "96cab3646a814b5e9f17b19318ac679514aea5f6"
      },
      {
        "path": "04_EXPERIMENTS/RECOVERY/SOURCE/EXP-0016_STRUCTURAL_RECOVERY.md",
        "sha": "80e5ec0df6b7238ebf698c977016cbb5f5d6874e"
      },
      {
        "path": "04_EXPERIMENTS/RECOVERY/SOURCE/EXP-0017_EXACT_RECOVERY_BASELINE.md",
        "sha": "f14cf81e16f7b5295424e6ba4b047b6a0a7acbda"
      },
      {
        "path": "04_EXPERIMENTS/RECOVERY/SOURCE/EXP-0018_RECOVERY_ORGAN.md",
        "sha": "3e8b2fc292ee82af6d182b2920b7c27d178741ad"
      },
      {
        "path": "04_EXPERIMENTS/RELATIONAL_MEMORY_ADAPTIVE_MEDIUM_RESULT_v0.1.md",
        "sha": "d320ab4c226d354d6d9536747127f8df710f9e30"
      },
      {
        "path": "04_EXPERIMENTS/RELATIONAL_MEMORY_PHYSICAL_DYNAMICS_RESULT_v0.1.md",
        "sha": "da851e81fb01b5c3534685d6f9e061ce3e7c470c"
      },
      {
        "path": "04_EXPERIMENTS/RELATION_CHANGE_ENTITY_RESULT_v0.1.md",
        "sha": "065453b418805c19e95c8e855d59e9c222454743"
      },
      {
        "path": "04_EXPERIMENTS/SPACE/README.md",
        "sha": "2360483634268435689036997a1fa86aec798a9a"
      },
      {
        "path": "04_EXPERIMENTS/SPACE/SOURCE/omega_anti_bh_v0_1.md",
        "sha": "bbdfcd886f63a4316c6f436b65555af8ffe0429a"
      },
      {
        "path": "04_EXPERIMENTS/SPACE/SOURCE/omega_anti_bh_v0_2.md",
        "sha": "588709717d8904abf50544fc2791255f86803313"
      },
      {
        "path": "04_EXPERIMENTS/SPACE/SOURCE/Ω-ANTI-BH_v0.1.md",
        "sha": "8a62d0c6b85952da35e2209dca360a679b63e424"
      },
      {
        "path": "04_EXPERIMENTS/STATE/README.md",
        "sha": "69c319b026477ef1f4df33df47009afe9b4caf37"
      },
      {
        "path": "04_EXPERIMENTS/SYSTEM_RELATION_CHANGE_UNDER_ENTITY_v0.1.md",
        "sha": "e59e7c0f90e5768b6848719b04133bcd4fe7109a"
      },
      {
        "path": "04_EXPERIMENTS/TOOLS/README.md",
        "sha": "a4c07f9eb01c037897ad32a91307750fb6e687d1"
      },
      {
        "path": "05_RESEARCH/2026-08-19_LIGHT_COLOR_ENTROPY.md",
        "sha": "eaf813ca41276601f6a7186ddff7defe4670be23"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/AUTONOMOUS_FULL_GRAPH_PASS_2026-08-24.md",
        "sha": "2df53f3340407bc7360ad551fc8d414b27bbea89"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/BOUNDARY-TRANSITION-COST-001.md",
        "sha": "a58d59d0ffe5e50e8f681c42fcb5616175d10745"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/CONSERVATION-RECIPROCAL-COUPLING-001.md",
        "sha": "6c483d7e426d9e808e3ea1e3e08c36eb76156578"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/CONTINUOUS_DISCRETE_FINITE_INFINITE_PASS_03_2026-08-24.md",
        "sha": "e7b9a3f776c94039278c9433617cc0b639279f6b"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/CROSS_INTERSECTION_PASS_2026-08-24.md",
        "sha": "e098f0fa84c0d63fcb139035b287ad57d5f8452c"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/EMERGENT_DIMENSION_FROM_CYCLES_2026-08-24.md",
        "sha": "792f32ddce9a01205bf5a41b66876389312c73a6"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/ENTITY_RELATION_WHOLE_CROSS_DOMAIN_TEST_2026-08-24.md",
        "sha": "9116de3e6248595a70ad4f7c69c36eb140dafd17"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/ENTITY_RELATION_WHOLE_FULL_CROSSDOMAIN_PASS_2026-08-24.md",
        "sha": "f2cc1457cd261bec0e521a673f7c6b22202fef0e"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/FOUNDATION_COMPLETE_ARCHITECTURE_2026-08-24.md",
        "sha": "78e34a58ec93487201cf6f7fd4da093244f65bd4"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/FOUNDATION_CROSSING_DERIVATION_PASS_2026-08-24.md",
        "sha": "296e5df23d863366b11c0c4de12454762095589c"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/FOUNDATION_CYCLE_CORE_2026-08-24.md",
        "sha": "ca58efd419609504fbfccbdb2a9c6469120601cf"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/FOUNDATION_DEPENDENCY_PASS_2026-08-24.md",
        "sha": "4ce6d018a8aacf490dba541e9488f636450833a3"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/FOUNDATION_FULL_AUDIT_2026-08-24.md",
        "sha": "8a5c403d19e87a91002d78c0f52e6e07fd809ee5"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/FOUNDATION_FUNDAMENTAL_PROPERTIES_2026-08-24.md",
        "sha": "8490f4d1f2f4263b14d430498daaa9dd737ff9ea"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/FOUNDATION_HIERARCHY_PASS_2026-08-24.md",
        "sha": "c5faaacdfe7245eaedb981d665ca0746e5dff748"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/FOUNDATION_INTERSECTION_MAP_2026-08-24.md",
        "sha": "ae217c9684acac59353da956df0917149642746c"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/FOUNDATION_MASTER_HIERARCHY_2026-08-24.md",
        "sha": "d80ec06e0e05f4f436e055b24e07ea4211a0695b"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/FOUNDATION_MASTER_STRUCTURE_2026-08-24.md",
        "sha": "47485bbcd315778c86edd76baa982b6320956004"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/FOUNDATION_OLD_NEW_CROSSCHECK_2026-08-24.md",
        "sha": "995ab87d8f2b2160f6459febe7c6b5f73c886c9d"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/FOUNDATION_PROOF_PROTOCOL_RESULT_2026-08-24.md",
        "sha": "bd200f2cfef9318f13659f54991cc6972ab0f0d0"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/FOUNDATION_REBUILD_PASS_2026-08-24.md",
        "sha": "7d140b0f6e0d1c366986be610f67f3207a26a586"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/FULL_RELATIONAL_GRAPH_2026-08-24.md",
        "sha": "563a0bf229bcbad42a169f137364f9dd8abb65af"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/FUNDAMENTAL_BRANCHES_EXPERIMENT_2026-08-24.md",
        "sha": "46bef19df5e0ac771ec56837d60bd4c2d47a9eb3"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/FUNDAMENTAL_DUALITIES_PASS_02_2026-08-24.md",
        "sha": "1d08560456190aa5344e133a4ef2510821bc6485"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/GENERATIONAL_CHAIN_TEST_2026-08-24.md",
        "sha": "6023c90e074762632c1c98e1030de5fcadd51f22"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/INVARIANT_NUMBER_PASS_2026-08-24.md",
        "sha": "cbb64df17e5a445496ddc4438d321fac2f9fc2e1"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/MASS-008_HIERARCHY_DEPENDENCY_TEST_2026-08-26.md",
        "sha": "fd08022b3a7fb63edd0b30b1ad42ca59e2851092"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/MASS_FUNDAMENTAL_BRANCH_2026-08-24.md",
        "sha": "7475feb47bac0b076020305dc7f09c42d92c2f50"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/RECURSIVE_GROWTH_PROBE_2026-08-25.md",
        "sha": "e0072fd559b3edf6d951fe831901e1242e8a8228"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/RESOURCE-EMERGENCE-001.md",
        "sha": "34fa2e5746bee45def11e1f0d20add81640cfd8d"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/RESOURCE_BOUNDED_GROWTH_PASS_2026-08-25.md",
        "sha": "2d47d1f925e61157cbbda4dd029b478e5e0e53ce"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/SCALE_FROM_STRUCTURE_PASS_2026-08-24.md",
        "sha": "16d2396213795e3a7246404b21dfa9d15b5a3926"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/SPATIALITY_IDENTITY_WILL_PROHIBITION_FULL_PASS_2026-08-24.md",
        "sha": "491b9a73914ac5f96cdc856842c871d2471fc7c0"
      },
      {
        "path": "05_RESEARCH/FOUNDATION/UTILITY_GUIDED_GROWTH_PASS_2026-08-25.md",
        "sha": "31f48fdc52c994e67e5216266c358a69a8dd60f9"
      },
      {
        "path": "05_RESEARCH/LIGHT_AS_INFORMATION_MEDIUM_v0.1.md",
        "sha": "266f1569154b27c1a6d9b3d047afab09db9f0a53"
      },
      {
        "path": "05_RESEARCH/LIGHT_COLOR_ENTROPY_v0.2.md",
        "sha": "e71fc7b67b5681f69849552d5b9fb421151cc9a3"
      },
      {
        "path": "05_RESEARCH/LIGHT_MEDIUM_MEMORY_SIM_v0.1.md",
        "sha": "8b12382fec8db4d53a3e211331419ce1e3fad0ca"
      },
      {
        "path": "05_RESEARCH/MEMORY_AS_CONSTRAINT_EXPERIMENT_v0.1.md",
        "sha": "ab3a169070b33f565c8feb40165ee6d86e6cfcda"
      },
      {
        "path": "05_RESEARCH/MEMORY_AS_CONSTRAINT_FULL_COMPUTATIONAL_TESTS_v0.1.md",
        "sha": "3a98c10a97500f73095da28bbe63af69b279df95"
      },
      {
        "path": "05_RESEARCH/MEMORY_AS_CONSTRAINT_GST_EVIDENCE_v0.2.md",
        "sha": "f30e0f5626eec0cd2bf71cde936f5283037f0006"
      },
      {
        "path": "05_RESEARCH/MEMORY_AS_CONSTRAINT_MATCHED_STATE_SIM_v0.1.md",
        "sha": "01f6584f4dd3c600e8a4150d7627ed7f4c92a25a"
      },
      {
        "path": "05_RESEARCH/MEMORY_AS_CONSTRAINT_PHYSICAL_CHECK_v0.2.md",
        "sha": "f2b321c98789a94b07ad54ae1781fddfb431a2ab"
      },
      {
        "path": "05_RESEARCH/MEMORY_AS_CONSTRAINT_VALIDATION_MATRIX_v0.1.md",
        "sha": "f3e2e90fd18cf11ca82cbf1de6954ef9eb76bee7"
      },
      {
        "path": "05_RESEARCH/MEMORY_AS_CONSTRAINT_VALIDATION_RESULT_v0.1.md",
        "sha": "49f7f8133038bbc24835a054c996389f7a19dedb"
      },
      {
        "path": "05_RESEARCH/METHODOLOGY_LEVEL_GUARD_v0.1.md",
        "sha": "b0ff65a40ad117d0dc359ecb42372ebb7c234f65"
      },
      {
        "path": "05_RESEARCH/OMEGA-Science/MASS/MASS-007_DYNAMIC_SCALE_HIERARCHY_RESULT_2026-08-26.md",
        "sha": "df54e00df3151394cb98fa03433fa82ccbc78175"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ALGORITHM_INVENTORY_v0.1.md",
        "sha": "f194cb47282ea336bd1e479c4c0957a2f7179e07"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ARCHITECTURE_PROPOSALS.md",
        "sha": "874c0f80df32799babf7b5f23af35db953784b03"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ARCHIVE_RECONCILIATION_2026-08-19.md",
        "sha": "0e3ce2dc5ee6f8cff11a07d2779e9c7ce0f033f0"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ARCHIVE_RECOVERY_RECONCILIATION_v0.1.md",
        "sha": "46f38e3ba781456f143d9c71d57ab570e30c1a41"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ATTRACTOR_SINK_CRITICALITY_RESULT_v0.2.md",
        "sha": "8c69ccb9be9b43e04f733fb693d04c1064ce88d6"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ATTRACTOR_SINK_EXCHANGE_EXPERIMENT_v0.1.md",
        "sha": "d3c2fb776eed3f27b3802d3032df5f5f56c3e48d"
      },
      {
        "path": "05_RESEARCH/ORGANISM/AUDIT_CHECKPOINT_2026-08-19.md",
        "sha": "d1736f588709f1ad5ccfca4f8ba7e63a5debf994"
      },
      {
        "path": "05_RESEARCH/ORGANISM/B-LAB_RECURSIVE_INVENTORY_v1.0.md",
        "sha": "85cb3b4021085b420881243772039a17f93345b5"
      },
      {
        "path": "05_RESEARCH/ORGANISM/B-LAB_RECURSIVE_INVENTORY_v1.1.md",
        "sha": "5632855bb021575be7b81ae69e65ecabed140127"
      },
      {
        "path": "05_RESEARCH/ORGANISM/BLACK_HOLE_CRITICAL_DENSITY_ACCESSIBILITY_TEST_v0.1.md",
        "sha": "ed199afd8b57b46d5de9436750cfbc3adf809b75"
      },
      {
        "path": "05_RESEARCH/ORGANISM/BLACK_HOLE_DENSE_NODE_SELF_CAPTURE_RESULT_v0.2.md",
        "sha": "15d36175da332c1ca9e5aaa0d68dc01c6338a16a"
      },
      {
        "path": "05_RESEARCH/ORGANISM/BLACK_HOLE_DENSE_NODE_SIM_v0.1.md",
        "sha": "4e43eef08d9178e6db6186054a772308925b683a"
      },
      {
        "path": "05_RESEARCH/ORGANISM/BLACK_HOLE_NORMALIZED_ESCAPE_RESULT_v0.1.md",
        "sha": "8379ce1d6c8c19228077304df327ed2e95fa50b0"
      },
      {
        "path": "05_RESEARCH/ORGANISM/BLACK_HOLE_RELATIONAL_CHECK_v0.2.md",
        "sha": "4774c90e0994aa85150c8c8716f08ec32a06b9b6"
      },
      {
        "path": "05_RESEARCH/ORGANISM/BLACK_HOLE_RELATION_INFORMATION_HYPOTHESIS_v0.1.md",
        "sha": "35d11640e8d5509dd884239a4aa2f3ec344968c3"
      },
      {
        "path": "05_RESEARCH/ORGANISM/BOUNDARY_ORDER_COUNTERMODEL_AUDIT_v0.1.md",
        "sha": "1d5c5c347a9373c81051f5c2688eee8975e51858"
      },
      {
        "path": "05_RESEARCH/ORGANISM/BOUNDARY_ORDER_COUNTERMODEL_EXPERIMENT_v0.1.md",
        "sha": "4529d837dc3bc3eaa7490dc1672ddfbbaf258c99"
      },
      {
        "path": "05_RESEARCH/ORGANISM/BOUNDARY_ORDER_COUNTERMODEL_RESULTS_v0.1.md",
        "sha": "d8e2904b1f7505f8de0854d03d199bfd67dae135"
      },
      {
        "path": "05_RESEARCH/ORGANISM/CLEANING_AS_MEMORY_REWRITE_v0.1.md",
        "sha": "f76ef6e63dbb688d19f9285a01d0686373cfd407"
      },
      {
        "path": "05_RESEARCH/ORGANISM/CLOSED_LOOP_SUPERLINEARITY_RESULT_v0.1.md",
        "sha": "3d533bac182534bdf0b1c13434242916bffeb396"
      },
      {
        "path": "05_RESEARCH/ORGANISM/EMERGENT_HORIZON_3D_RELATIONAL_TEST_v0.1.md",
        "sha": "16afc161fae3bab9a9a66b83541a81b369424c62"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ENDOGENOUS_ATTRACTION_CRITICAL_THRESHOLD_RESULT_v0.1.md",
        "sha": "206bab7ffd498f25a85321d1d3145ec378543009"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ENDOGENOUS_RELATIONAL_ATTRACTION_CONTROL_v0.1.md",
        "sha": "630e86defdba71e76218778b7a517685c44c8e47"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ENDOGENOUS_RELEASE_RESULT_v0.1.md",
        "sha": "acc9adfa0be8c1f792b6561b0e532efc99edc0db"
      },
      {
        "path": "05_RESEARCH/ORGANISM/END_OF_DAY_ASSESSMENT_2026-08-19.md",
        "sha": "d64e5298694252452fe74089b91d7d6a089203c3"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ENERGY_CONSERVING_NETWORK_CRITICALITY_v0.1.md",
        "sha": "ed5bfacbaf14a7561286d23b06e549717109f73e"
      },
      {
        "path": "05_RESEARCH/ORGANISM/EVIDENCE_COVERAGE_MATRIX_v0.1.md",
        "sha": "984284c3dc21a3617bd6182cc7a141ced48a1154"
      },
      {
        "path": "05_RESEARCH/ORGANISM/EVIDENCE_INDEX.md",
        "sha": "92abddea90a3472057ed794b601f083acfa86d1e"
      },
      {
        "path": "05_RESEARCH/ORGANISM/EXACT_COPY_AUDIT_v1.0.md",
        "sha": "7da77b9debde99553e129e416751f28160e759ca"
      },
      {
        "path": "05_RESEARCH/ORGANISM/EXECUTION_LOG_2026-08-19.md",
        "sha": "b1b146fe1450b61f087839f1479c6ff1779a178e"
      },
      {
        "path": "05_RESEARCH/ORGANISM/EXECUTION_RESULT_HISTORY_RECONCILIATION_v0.1.md",
        "sha": "513869fc959307c41233e6aa295cf733c5e8836b"
      },
      {
        "path": "05_RESEARCH/ORGANISM/EXPERIMENT_STATUS_2026-08-20.md",
        "sha": "d8fed5341f175a0566339f3f5e09bf46720803d6"
      },
      {
        "path": "05_RESEARCH/ORGANISM/FINAL_CONTROL_MATRIX_v1.0.md",
        "sha": "5decf96ab1850745890a8d0da1ef5c882e3db4aa"
      },
      {
        "path": "05_RESEARCH/ORGANISM/FINAL_NORMATIVE_STATE_2026-08-19.md",
        "sha": "ba4e11f66a9d830cccfa54e540b7bb0ed9341f06"
      },
      {
        "path": "05_RESEARCH/ORGANISM/FIRE_PLASMA_CLEANING_HYPOTHESIS_v0.1.md",
        "sha": "fa966839d2cd621f219e5d80049e2003f44a1374"
      },
      {
        "path": "05_RESEARCH/ORGANISM/FOUNDATIONAL_ORIENTATION_REGISTER_v0.1.md",
        "sha": "63a48feb991d5c78b17162f5896414985121655b"
      },
      {
        "path": "05_RESEARCH/ORGANISM/FOUNDATION_LINK.md",
        "sha": "78befb2360bc2804acfed0e2c434d179dd290ad3"
      },
      {
        "path": "05_RESEARCH/ORGANISM/FOUNDATION_MEMORY_AS_CONSTRAINT_v0.1.md",
        "sha": "b9b86920f1ce547c686bc5aeec687f82a83139bd"
      },
      {
        "path": "05_RESEARCH/ORGANISM/FOUNDATION_PATTERN_INVENTORY_v0.1.md",
        "sha": "c3007b0d32809bd8f6f31283f115518984ff0fba"
      },
      {
        "path": "05_RESEARCH/ORGANISM/FOUNDATION_REBUILD_WORKPLAN_v0.1.md",
        "sha": "5e77d0bd49df1b743dccca2624032bc22c8cb1ca"
      },
      {
        "path": "05_RESEARCH/ORGANISM/FOUNDATION_TRACEABILITY_MATRIX_v0.1.md",
        "sha": "05e4bcf36faf896c106ed39890be3702137bf90b"
      },
      {
        "path": "05_RESEARCH/ORGANISM/FULL_TRANSFER_MATRIX.md",
        "sha": "1b9fed5030d5e2cc29d60d9fa4a6fb935a6fc5fb"
      },
      {
        "path": "05_RESEARCH/ORGANISM/FULL_TRANSFER_MATRIX_v2.md",
        "sha": "184f9b73e059e90779e44d8d011d540ec56266de"
      },
      {
        "path": "05_RESEARCH/ORGANISM/FUNDAMENTAL_CANDIDATE_ANALYSIS_v0.1.md",
        "sha": "b26a39efce59bfa9835a9f81ae85238473a8b7e7"
      },
      {
        "path": "05_RESEARCH/ORGANISM/GRAPH_INVENTORY_v0.1.md",
        "sha": "7b465350201c2cdc0fca0ccd722fbe0d10f1be9c"
      },
      {
        "path": "05_RESEARCH/ORGANISM/GUARDIAN/REBUILD/CONTINUING_LOAD_TEST_2026-08-24.md",
        "sha": "b71f138e740c315ec074de96d9e6b324f7748777"
      },
      {
        "path": "05_RESEARCH/ORGANISM/GUARDIAN/REBUILD/GUARDIAN_REBUILD_v0.2_TEST_2026-08-24.md",
        "sha": "dc82e5db771c340fdb1342d78d6cc3cb298b5d73"
      },
      {
        "path": "05_RESEARCH/ORGANISM/GUARDIAN/REBUILD/GUARDIAN_REBUILD_v0.2_WORKING.md",
        "sha": "e56e57b80bf261aa1ff40b2073ea129d5f3e0f49"
      },
      {
        "path": "05_RESEARCH/ORGANISM/GUARDIAN/REBUILD/GUARDIAN_WORKING_PROTOCOL_v0.1.md",
        "sha": "d1ae0f6de4b343aa42e4ac86461da98c533db894"
      },
      {
        "path": "05_RESEARCH/ORGANISM/GUARDIAN/REBUILD/GUARDIAN_WORK_LOG_2026-08-24.md",
        "sha": "00f672f008cff707b70d0dee926bc0f48b8da527"
      },
      {
        "path": "05_RESEARCH/ORGANISM/GUARDIAN/REBUILD/VERIFY_STRESS_FINDINGS_v0.1.md",
        "sha": "2f925e746464baafa663eb4e086ad4a9c8306a0e"
      },
      {
        "path": "05_RESEARCH/ORGANISM/HISTORY_STRUCTURE_RECONCILIATION_v0.1.md",
        "sha": "fae52ef86cbbe2bc2dd3f1d8e607717d836ca53a"
      },
      {
        "path": "05_RESEARCH/ORGANISM/INTER_ORGAN_RELATION_EVIDENCE_MATRIX_v0.1.md",
        "sha": "5a4000b72461e3f5bcab5b3e4121f407bd118b65"
      },
      {
        "path": "05_RESEARCH/ORGANISM/INVENTORY_COMPLETION_STATUS_v0.1.md",
        "sha": "448e3c14f3e95e5ea2dc53586d2c53b9efcf04a4"
      },
      {
        "path": "05_RESEARCH/ORGANISM/LAYER_CLASSIFICATION_MATRIX_v0.1.md",
        "sha": "684b9336fd1b104bbafb94a85df7ec23b30643f9"
      },
      {
        "path": "05_RESEARCH/ORGANISM/LOSS_AUDIT_REGISTER_v1.0.md",
        "sha": "043b66721f52b48c65b54f037855fb7acb1aecb0"
      },
      {
        "path": "05_RESEARCH/ORGANISM/MASTER_CLASSIFICATION_MATRIX_v0.1.md",
        "sha": "f64e467150533bc2e443b29ccfbc4c5b45c4ee73"
      },
      {
        "path": "05_RESEARCH/ORGANISM/MEMORY_AS_STRUCTURAL_STATE_FINAL_GATE_v0.1.md",
        "sha": "d5e1e86cd5ce439003802e38da0345d37a8b54ec"
      },
      {
        "path": "05_RESEARCH/ORGANISM/MEMORY_LIMITS_PHASES_v0.1.md",
        "sha": "f30c5c9fe495006388fce962233bbb790f0f2560"
      },
      {
        "path": "05_RESEARCH/ORGANISM/MINIMAL_FOUNDATION_COUNTERMODEL_AUDIT_v0.1.md",
        "sha": "a9c42d1ac4f3caf417e05cd17a2ee752e2ae9bd5"
      },
      {
        "path": "05_RESEARCH/ORGANISM/MINIMAL_FOUNDATION_COUNTERMODEL_EXPERIMENT_v0.1.md",
        "sha": "f3faef5b052080852acb2dab57a3005656eb2245"
      },
      {
        "path": "05_RESEARCH/ORGANISM/MINIMAL_FOUNDATION_COUNTERMODEL_RESULTS_v0.1.md",
        "sha": "f0d6c752bb9d797eced480a0c781bb2c7f97013f"
      },
      {
        "path": "05_RESEARCH/ORGANISM/MINIMAL_FOUNDATION_STORY_v0.1.md",
        "sha": "07b08b6e028fcab87df3c52daab93e0e696c059e"
      },
      {
        "path": "05_RESEARCH/ORGANISM/MINIMAL_RELATIONAL_MEMORY_LAW_RESULT_v0.1.md",
        "sha": "ff5ef8802b43ef0284b219e7d274f4ef6c802591"
      },
      {
        "path": "05_RESEARCH/ORGANISM/MINIMAL_RELATIONAL_MEMORY_SCALE_CONTROL_v0.2.md",
        "sha": "fc846da0273076fbf7b91a921cbb1303121a49d6"
      },
      {
        "path": "05_RESEARCH/ORGANISM/NORMATIVE_INVARIANTS_v0.1.md",
        "sha": "8a2a0cd5d7afa1fe11d4eef6a85085c1914eae30"
      },
      {
        "path": "05_RESEARCH/ORGANISM/NORMATIVE_WORK_QUEUE_v0.1.md",
        "sha": "f878f81ad96f53e4aab157b0e4909559aadb09fc"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ONTOLOGY_VS_ENGINEERING_MATRIX_v0.1.md",
        "sha": "aa35dddfe98cbec1c61e97e5a690db423f688db8"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ORGANISM_HISTORY.md",
        "sha": "35d34b2fd03ce4831fdd81f96033b37151b9886f"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ORGANISM_PASSPORT.md",
        "sha": "3209a6c8465320b57e33d6acd934bc420640e5ed"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ORGANISM_RESEARCH_JOURNAL.md",
        "sha": "e6285015409e75b0dc23dde0a8276d814771ea10"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ORGANISM_RESEARCH_PLAN.md",
        "sha": "8b9bf88c565c512487a9a4dcc35690878b05ddf0"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ORGAN_CHRONOLOGY_REGISTER_v1.0.md",
        "sha": "04dfb932706b6d53288a8ffb4daea092fdc15721"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ORGAN_INVENTORY_MATRIX_v0.1.md",
        "sha": "d0884613ffd7a549de0343978eceb5b7ba4b2ab5"
      },
      {
        "path": "05_RESEARCH/ORGANISM/ORGAN_STRUCTURE_RECONCILIATION_v0.1.md",
        "sha": "56fb5d7760c4d59689df9ea72b98250474068ea0"
      },
      {
        "path": "05_RESEARCH/ORGANISM/PROJECT_ALGORITHM_CODE_RECONCILIATION_v0.1.md",
        "sha": "cd3d54a6eefad8fe3d7b4dc685478df4a9fe8143"
      },
      {
        "path": "05_RESEARCH/ORGANISM/README.md",
        "sha": "9f730ad474804bf27e13c6789aceee08db149290"
      },
      {
        "path": "05_RESEARCH/ORGANISM/RECONCILIATION_LEDGER_v1.0.md",
        "sha": "b367c20da9bd472f2d027acb2ff2890f1f5abe94"
      },
      {
        "path": "05_RESEARCH/ORGANISM/RECONCILIATION_PASS_1_2_2026-08-26.md",
        "sha": "b09494fc42db4ee75fa27919a5a4bb0cb87259dc"
      },
      {
        "path": "05_RESEARCH/ORGANISM/RECOVERY_EVIDENCE_CHAIN_v1.0.md",
        "sha": "ada08a7312a5f8716327e13bca2e4684224f4bc2"
      },
      {
        "path": "05_RESEARCH/ORGANISM/REINFORCEMENT_EXPONENT_CRITICALITY_RESULT_v0.1.md",
        "sha": "3e0f395f44f301b060787e3c2ebf42a5ca3e6493"
      },
      {
        "path": "05_RESEARCH/ORGANISM/RELATIONAL_MEMORY_ENDOGENOUS_CONDENSATION_v0.1.md",
        "sha": "8da93e35962db1288cc4ad6cf2db2f95e1207403"
      },
      {
        "path": "05_RESEARCH/ORGANISM/RELATIONAL_MEMORY_FINAL_CONTROL_2026-08-20.md",
        "sha": "8c571490b1d49dd32e8a66e079db3caddac221ee"
      },
      {
        "path": "05_RESEARCH/ORGANISM/RELATIONAL_MEMORY_HIDDEN_HISTORY_RESULT_v0.1.md",
        "sha": "3dd0604930afc7e03c1cda38a99a5b57199770eb"
      },
      {
        "path": "05_RESEARCH/ORGANISM/RELATIONAL_MEMORY_KERNEL_INDEPENDENCE_RESULT_v0.1.md",
        "sha": "fa884bfd180200cf3cb2409298fbc6dacca84218"
      },
      {
        "path": "05_RESEARCH/ORGANISM/RELATIONAL_MEMORY_KERNEL_INDEPENDENCE_v0.1.md",
        "sha": "d773004631f365e420edb2bf5edae5219bdeffbd"
      },
      {
        "path": "05_RESEARCH/ORGANISM/RELATIONAL_MEMORY_MATCHED_PRESENT_RESULT_v0.1.md",
        "sha": "2cff934b918d5135ad28e774b3b83e478bb9b39a"
      },
      {
        "path": "05_RESEARCH/ORGANISM/RELATIONAL_MEMORY_PRIMITIVE_LAW_TEST_v0.1.md",
        "sha": "778d1cadfb1276c593582523c982badbc8445191"
      },
      {
        "path": "05_RESEARCH/ORGANISM/RELATIONAL_MEMORY_TEMPORAL_ORDER_EXPERIMENT_v0.1.md",
        "sha": "fa55ddcb0217d0f9347a170c0d9097cffebd72f5"
      },
      {
        "path": "05_RESEARCH/ORGANISM/RELATIONAL_MEMORY_TEMPORAL_ORDER_RESULT_v0.1.md",
        "sha": "d0fbaddc5bc7f560dc7d4b4631418ece244405cc"
      },
      {
        "path": "05_RESEARCH/ORGANISM/RELATIONAL_MEMORY_TEMPORAL_ORDER_TEST_v0.1.md",
        "sha": "0584bb99c004780315d0ec5f1ec8472e47849bd7"
      },
      {
        "path": "05_RESEARCH/ORGANISM/RELATION_EVIDENCE_REGISTER_v1.0.md",
        "sha": "80ce8d9a44cf50a9a6d19f8a5035ae65f5844ed0"
      },
      {
        "path": "05_RESEARCH/ORGANISM/RELATION_MEMORY_CLEANING_MATHEMATICAL_RESULT_v0.1.md",
        "sha": "09236fcc7d110f25df8213c4bbe63c9fa6bd4227"
      },
      {
        "path": "05_RESEARCH/ORGANISM/REPRESENTATIVE_ORGAN_COMPARISON_v0.1.md",
        "sha": "27422394dea9e9379a3b8c073af094125dfa108e"
      },
      {
        "path": "05_RESEARCH/ORGANISM/RESEARCH_PROTOCOL.md",
        "sha": "fdfa460c09f348c0ff921085abe0d55559963802"
      },
      {
        "path": "05_RESEARCH/ORGANISM/SOURCE_INVENTORY/B-LAB.md",
        "sha": "6d856c20cc92c832e0545610a67da9fc6ba18c5f"
      },
      {
        "path": "05_RESEARCH/ORGANISM/SOURCE_INVENTORY/BENCHMARKS-B-LAB.md",
        "sha": "deec398872d3451db4d4d61fbadcd136ea71276f"
      },
      {
        "path": "05_RESEARCH/ORGANISM/SOURCE_INVENTORY/MARKET.md",
        "sha": "ca8af6a59388c4898879881f74b9175cb86cdd07"
      },
      {
        "path": "05_RESEARCH/ORGANISM/SOURCE_INVENTORY/SPACE.md",
        "sha": "37fb9c7f3892de833ce1659f4d1b9229ee6c37bd"
      },
      {
        "path": "05_RESEARCH/ORGANISM/SOURCE_INVENTORY_B-LAB_v1.0.md",
        "sha": "9ef8177e93d6ac1a3ba97d6bc5cdb9322cd8ccb4"
      },
      {
        "path": "05_RESEARCH/ORGANISM/SOURCE_TRANSFER_COMPLETE.md",
        "sha": "61d5e858e6510a378a8b40513dcd2c305e5ddeae"
      },
      {
        "path": "05_RESEARCH/ORGANISM/STANDARD_RECONCILIATION_v0.1.md",
        "sha": "63a383e4c9d54ec686c224130420339d5ba0063f"
      },
      {
        "path": "05_RESEARCH/ORGANISM/STATUS_GATE.md",
        "sha": "c5e85acee31c652230d44f22bd3c1bf90368530c"
      },
      {
        "path": "05_RESEARCH/ORGANISM/STIFFNESS_CONNECTIVITY_ATTRACTION_PLAN_v0.1.md",
        "sha": "5e4673d44b8d9c5ae7466525744c3d34eff02196"
      },
      {
        "path": "05_RESEARCH/ORGANISM/STIFFNESS_CONNECTIVITY_ATTRACTION_RESULT_v0.1.md",
        "sha": "4689d59fb607ed2ab64bc83c6c3faed4178acc6e"
      },
      {
        "path": "05_RESEARCH/ORGANISM/STRUCTURAL_MEMORY_CHOICE_GATE_v0.1.md",
        "sha": "03176d44a10051a3c360ac32da7b3515738c0d86"
      },
      {
        "path": "05_RESEARCH/ORGANISM/STRUCTURAL_MEMORY_TO_SUPERLINEAR_FEEDBACK_RESULT_v0.1.md",
        "sha": "d71647a6b1a6f1fc8769ace71474d927b8d057cb"
      },
      {
        "path": "05_RESEARCH/ORGANISM/SYSTEM_FOUNDATION_RECONCILIATION_v1.0.md",
        "sha": "0fe2ab5dedfe3034c2b4b46fd755c92dc290a964"
      },
      {
        "path": "05_RESEARCH/ORGANISM/WORKING_STATE_GATE_v1.0.md",
        "sha": "b23462cdfc4e2510c5cb3168101fd4051a43abec"
      },
      {
        "path": "05_RESEARCH/ORGANS/AUDIT/DOSSIER.md",
        "sha": "a1a2899bc10878e92e64ab2f98b1796e8e155101"
      },
      {
        "path": "05_RESEARCH/ORGANS/EXECUTION/DOSSIER.md",
        "sha": "77a0a6500bbb296fd1af68bcb47b4e8bf20f5e55"
      },
      {
        "path": "05_RESEARCH/ORGANS/FEEDBACK/DOSSIER.md",
        "sha": "b77dc5be69cc89a8a8b8e07fb6fde4f208e0effb"
      },
      {
        "path": "05_RESEARCH/ORGANS/GRAPH/DOSSIER.md",
        "sha": "e25f106dbd9fd11f3d2bddebac72899e1dfedebe"
      },
      {
        "path": "05_RESEARCH/ORGANS/GUARDIAN/DOSSIER.md",
        "sha": "343876ff11f930078499cd71d710a23047623d06"
      },
      {
        "path": "05_RESEARCH/ORGANS/LAB/DOSSIER.md",
        "sha": "278776100d4ac864135d768cd00d23ff703d757f"
      },
      {
        "path": "05_RESEARCH/ORGANS/MEMORY/DOSSIER.md",
        "sha": "3482282369e5ea64816640d9c9bc3dc60b8ad631"
      },
      {
        "path": "05_RESEARCH/ORGANS/PERCEPTION/DOSSIER.md",
        "sha": "1faff4fc13922b311472aa2e1e0faffaf857a480"
      },
      {
        "path": "05_RESEARCH/ORGANS/PLANNING/DOSSIER.md",
        "sha": "2195a33d1a789ca0e8d29f9e36da377b75456319"
      },
      {
        "path": "05_RESEARCH/ORGANS/REASONING/DOSSIER.md",
        "sha": "fa4b950d5b2ac7d94f9232bcb161a3b9664c9265"
      },
      {
        "path": "05_RESEARCH/ORGANS/RECOVERY/CI_LINEAGE.md",
        "sha": "ae4ebf75c52cabcaae037a900876af4d261959ab"
      },
      {
        "path": "05_RESEARCH/ORGANS/RECOVERY/DOSSIER.md",
        "sha": "38723e6a519d17512631c2dd8c0a6708c9084362"
      },
      {
        "path": "05_RESEARCH/ORGANS/RECOVERY/EXPERIMENTS/EXP-0013.md",
        "sha": "9b6a391472785525e78f723e71d7c9c793a8365a"
      },
      {
        "path": "05_RESEARCH/ORGANS/RECOVERY/EXPERIMENTS/EXP-0014.md",
        "sha": "d868a7d454060c79c2538a0391ab4e88fcf46687"
      },
      {
        "path": "05_RESEARCH/ORGANS/RECOVERY/EXPERIMENTS/EXP-0015.md",
        "sha": "96cab3646a814b5e9f17b19318ac679514aea5f6"
      },
      {
        "path": "05_RESEARCH/ORGANS/RECOVERY/EXPERIMENTS/EXP-0016.md",
        "sha": "80e5ec0df6b7238ebf698c977016cbb5f5d6874e"
      },
      {
        "path": "05_RESEARCH/ORGANS/RECOVERY/EXPERIMENTS/EXP-0017.md",
        "sha": "f14cf81e16f7b5295424e6ba4b047b6a0a7acbda"
      },
      {
        "path": "05_RESEARCH/ORGANS/RECOVERY/EXPERIMENTS/EXP-0018.md",
        "sha": "3e8b2fc292ee82af6d182b2920b7c27d178741ad"
      },
      {
        "path": "05_RESEARCH/ORGANS/RECOVERY/EXPERIMENT_EVIDENCE_REGISTER.md",
        "sha": "12399d6779e0864110d36b7a9573b74c21aa22b7"
      },
      {
        "path": "05_RESEARCH/ORGANS/SPACE/DOSSIER.md",
        "sha": "8e3d99b18eee9589c4bbcf8e494ac88389904fe2"
      },
      {
        "path": "05_RESEARCH/ORGANS/STATE/DOSSIER.md",
        "sha": "6d37dbf8b5432a7ebe515c1894d6879f9321b4a4"
      },
      {
        "path": "05_RESEARCH/ORGANS/TOOLS/DOSSIER.md",
        "sha": "9e54a5d458b5c9917d0a378cf155abafd0722b3a"
      },
      {
        "path": "05_RESEARCH/ORISIK_2026-08-20_TIME_THERMODYNAMICS.md",
        "sha": "6eb49cca17fb14aabc5bf6d6a69f502a7ff895bc"
      },
      {
        "path": "05_RESEARCH/ORISIK_LIGHT_INFORMATION.md",
        "sha": "84ab383300537447687dbee66285383a9b509be7"
      },
      {
        "path": "05_RESEARCH/R01_INDEPENDENT_REPLICATION_RESULTS_v1.0.md",
        "sha": "c5d35e14b2d37729a1f4ffe1c34bddebb2a2c380"
      },
      {
        "path": "05_RESEARCH/R01_INDEPENDENT_REPLICATION_v1.0.py",
        "sha": "a2af0d465c7c800ec30889a312c5f8f1753acbcd"
      },
      {
        "path": "05_RESEARCH/README.md",
        "sha": "c38de4affbd507441425499e6de062135ad848c6"
      },
      {
        "path": "06_ARCHIVE/Guardian/SECURITY_TEST_MATRIX.md",
        "sha": "697f8dddda3a4c20d008df40f4003b20e7c3c203"
      },
      {
        "path": "09_CURRENT/RESEARCH_STATE.md",
        "sha": "c107acd3d1a7a2fbd6b8bd69a9b1b6c8b5023f2d"
      },
      {
        "path": "10_CONTROL/RESEARCH_CONTROL_CHECKLIST.md",
        "sha": "049151c12f491c1abc030a432d501286b91ba9c6"
      },
      {
        "path": "CODE/CL-SCALING-002/test_process_workers.py",
        "sha": "e96435aef3624819f960b3f21760d690a7532980"
      }
    ],
    "ARCHIVE": [
      {
        "path": "foundation/ANALYSIS_INDEX_v1.0.md",
        "sha": "e2bdce4a84e3c6b425f0e51172b7470f6d7bd8f3"
      },
      {
        "path": "imports/SPACE-2026-08-15/test-evidence.md",
        "sha": "e2c4f40c92c83c06dd9fe3fc44e637fe3333513b"
      }
    ]
  }
}
```
