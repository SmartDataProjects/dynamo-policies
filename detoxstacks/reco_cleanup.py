from detox.policy import Policy
import detox.policies.policies import *

default = Policy.DEC_PROTECT

exceptions = ActionList()
exceptions.add_action('Keep', '*', '/HLTPhysics/CMSSW_7_4_14-2015_10_20_newconditions0_74X_dataRun2_HLTValidation_Candidate_2015_10_12_10_41_09-v1/RECO')
exceptions.add_action('Keep', '*', '/HLTPhysics/CMSSW_7_4_14-2015_10_20_reference_74X_dataRun2_HLT_v2-v1/RECO')
exceptions.add_action('Keep', '*', '/ZeroBias*/Run2015A-PromptReco-v1/RECO')
exceptions.add_action('Keep', '*', '/*TOTEM*/*Run2015D*/RECO')

rule_stack = [
    ProtectIncomplete(),
    exceptions,
    DeleteByNameOlderThan(180., 'd', '/*/*/RECO', use_dataset_time = True),
    DeleteByNameOlderThan(180., 'd', '/*/*LogError*/RAW-RECO', use_dataset_time = True),
    DeleteByNameOlderThan(60., 'd', '/*/*/RAW', use_dataset_time = True)
]
