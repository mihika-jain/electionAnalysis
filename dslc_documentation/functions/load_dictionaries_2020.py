import sys
def dictionary():
    dictionary = {
      "V200002" : {"column": "interviewMode", "unique_values": 3, "type":"cat"},
      "V200010b": {"column": "weights", "unique_values": sys.maxsize, "type": "num"},
      "V201033": {"column": "PRE_VotePresident", "unique_values": 5, "type": "cat"},
      "V201144x": {"column": "PRE_approvalOfPresidentCovidResponse", "unique_values": 4, "type":"rank"},
      "V201218": {"column": "PRE_RaceOutcomePrediction", "unique_values": 2, "type": "cat"},
      "V201151": {"column": "PRE_ThermoBiden", "unique_values": 100, "type": "rank"},
      "V201152": {"column": "PRE_ThermoTrump", "unique_values": 100, "type": "rank"},
      "V201153": {"column": "PRE_ThermoHarris", "unique_values": 100, "type": "rank"},
      "V201154": {"column": "PRE_ThermoPence", "unique_values": 100, "type": "rank"},
      "V201155": {"column": "PRE_ThermoObama", "unique_values": 100, "type": "rank"},
      "V201156": {"column": "PRE_ThermoDemParty", "unique_values": 100, "type": "rank"},
      "V201157": {"column": "PRE_ThermoRepParty", "unique_values": 100, "type": "rank"},
      "V201553": {"column": "PRE_ParentNativeStatus", "unique_values": 3, "type": "cat"},
      "V201587": {"column": "PRE_YearsAtAddress", "unique_values": 40, "type": "num"},
      "V201600": {"column": "Sex", "unique_values": 2, "type": "cat"},
      "V201225x": {"column": "PRE_SummaryVoteDutyChoice", "unique_values": 7, "type": "rank"},
      "V201231x": {"column": "PRE_PartyID", "unique_values": 7, "type": "rank"},
      "V201246": {"column": "PRE_ScaleSpendingServices", "unique_values": 7, "type": "rank"},
      "V201433" : {"column": "PRE_religionImportance", "unique_values":5, "type":"rank"},
      #"V201018": {"column": "PRE_PartyRegistration", "unique_values": 4, "type": "cat"},
      "V201115": {"column": "PRE_CountryDirection", "unique_values": 5, "type": "rank"},
      "V201233": {"column": "PRE_GovTrust", "unique_values": 5, "type": "rank"},
      "V201324": {"column": "PRE_EconomyView", "unique_values": 5, "type": "rank"},
      "V201340": {"column": "PRE_AbortionRightsSC", "unique_values": 3, "type": "cat"},
      "V201507x": {"column": "Age", "unique_values": 80, "type": "num"},
      "V201510": {"column": "EducationLevel", "unique_values": 8, "type": "cat"},
      "V201517": {"column": "WorkStatus", "unique_values": 2, "type": "cat"},
      "V201617x": {"column": "Income", "unique_values": 22, "type": "rank"},
      "V201549x": {"column": "Race", "unique_values": 6, "type": "cat"},
      "V202054x": {"column": "StateRegistration", "unique_values": 56, "type": "cat"},
      "V201567": {"column": "HouseholdChildren", "unique_values": 5, "type": "rank"},
      "V201630b": {"column": "PRE_Fox_Hannity", "unique_values": 2, "type": "cat"},
      "V201630c": {"column": "PRE_Fox_TuckerCarlsonTonight", "unique_values": 2, "type": "cat"},
      "V201630k": {"column": "PRE_Fox_SpecialReportBretBaier", "unique_values": 2, "type": "cat"},
      "V201630f": {"column": "PRE_Fox_TheFive", "unique_values": 2, "type": "cat"},
      "V201630g": {"column": "PRE_Fox_TheIngrahamAngle", "unique_values": 2, "type": "cat"},
      "V201630h": {"column": "PRE_Fox_TheStoryMarthaMacCallum", "unique_values": 2, "type": "cat"},
      "V201631k": {"column": "PRE_Fox_FoxAndFriends", "unique_values": 2, "type": "cat"},
      "V201634f": {"column": "PRE_Fox_FoxNewsWebsite", "unique_values": 2, "type": "cat"},
      "V201630i": {"column": "PRE_CNN_TheLeadJakeTapper", "unique_values": 2, "type": "cat"},
      "V201630j": {"column": "PRE_CNN_AndersonCooper360", "unique_values": 2, "type": "cat"},
      "V201630q": {"column": "PRE_CNN_CuomoPrimeTime", "unique_values": 2, "type": "cat"},
      "V201631b": {"column": "PRE_CNN_ErinBurnettOutFront", "unique_values": 2, "type": "cat"},
      "V201634b": {"column": "PRE_CNN_CNNWebsite", "unique_values": 2, "type": "cat"},
      "V201630n": {"column": "PRE_ABC_WorldNewsTonight", "unique_values": 2, "type": "cat"},
      "V201631d": {"column": "PRE_ABC_2020", "unique_values": 2, "type": "cat"},
      "V201631i": {"column": "PRE_ABC_GoodMorningAmerica", "unique_values": 2, "type": "cat"},
      "V201646": {"column": "PRE_PartyMoreHouseMembers", "unique_values": 2, "type": "cat"},
      "V201645": {"column": "PRE_FederalSpendingKnowledge", "unique_values": 4, "type": "cat"},
      "V201351": {"column": "PRE_VoteAccuracy", "unique_values": 5, "type": "rank"},
      "V201650": {"column": "PRE_SurveySeriousness", "unique_values": 5, "type": "rank"},
      "V201249": {"column": "PRE_ScaleDefenseSpending", "unique_values": 7, "type": "rank"},
      "V201252": {"column": "PRE_ScaleMedInsurance", "unique_values": 7, "type": "rank"},
      "V201380": {"column": "PRE_CorruptionView", "unique_values": 3, "type": "cat"},
      "V201246": {"column": "PRE_ScaleGovAssistance", "unique_values": 7, "type": "rank"},
      "V201255": {"column": "PRE_ScaleJobIncome", "unique_values": 7, "type": "rank"},
      "V202051": {"column": "POST_RegistrationStatus", "unique_values": 3, "type": "cat"},
      "V202068x": {"column": "POST_Voted2020", "unique_values": 3, "type": "cat"},
      "V202073": {"column": "POST_VotePresident", "unique_values": 4, "type": "cat"},
      "V202219": {"column": "POST_VoteAccuracy", "unique_values": 5, "type": "rank"},
      "V202156": {"column": "POST_ThermoHarris", "unique_values": 100, "type": "rank"},
      "V202157": {"column": "POST_ThermoPence", "unique_values": 100, "type": "rank"},
      "V202143": {"column": "POST_ThermoBiden", "unique_values": 100, "type": "rank"},
      "V202144": {"column": "POST_ThermoTrump", "unique_values": 100, "type": "rank"},
      "V202123": {"column": "POST_ReasonNotVoting", "unique_values": 15, "type": "cat"},
      "V202205y1": {"column": "POST_ProblemMention", "unique_values": 82, "type": "cat"},
      #"V202580": {"column": "POST_ScaleMedInsurance", "unique_values": 7, "type": "rank"},
      #"V202624": {"column": "POST_HealthSpending", "unique_values": 7, "type": "rank"},
      "V202644": {"column": "POST_RespondentHonesty", "unique_values": 3, "type": "cat"}
    }
    return dictionary


def column_labels():
    column_labels = {
        "V200002":{
            "column": "interviewMode",
            "labels":{
                1: "Video", 
                2: "Telephone", 
                3: "Web"
            }
        },
        "V201033": {
            "column": "PRE_VotePresident",
            "labels": {
                1: "Joe Biden",
                2: "Donald Trump",
                3: "Jo Jorgensen",
                4: "Howie Hawkins",
                5: "Other"
            }
        },
        "V201218": {
            "column": "PRE_RaceOutcomePrediction",
            "labels": {
                1: "Will be close",
                2: "Win by quite a bit"
            }
        },
        "V201553": {
            "column": "PRE_ParentNativeStatus",
            "labels": {
                1: "Both parents born in the US",
                2: "One parent born in the US",
                3: "Both parents born in another country"
            }
        },
        "V201600": {
            "column": "Sex",
            "labels": {
                1: "Male",
                2: "Female"
            }
        },
        "V201340": {
            "column": "PRE_AbortionRightsSC",
            "labels": {
                1: "Pleased",
                2: "Upset",
                3: "Neither pleased nor upset"
            }
        },
        "V201510": {
            "column": "EducationLevel",
            "labels": {
                1: "Less than high school credential",
                2: "High school graduate",
                3: "Some college but no degree",
                4: "Associate degree - occupational/vocational",
                5: "Associate degree - academic",
                6: "Bachelor’s degree",
                7: "Master’s degree",
                8: "Professional/Doctoral degree",
            }
        },
        "V201517": {
            "column": "WorkStatus",
            "labels": {
                1: "Yes",
                2: "No, did not work (or retired)"
            }
        },
        "V201549x": {
            "column": "Race",
            "labels": {
                1: "White, non-Hispanic",
                2: "Black, non-Hispanic",
                3: "Hispanic",
                4: "Asian/Pacific Islander, non-Hispanic",
                5: "Native American/Alaska Native, non-Hispanic",
                6: "Multiple races, non-Hispanic"
            }
        },
        "V202054x": {
            "column": "StateRegistration",
            "labels": {
                1: "Alabama",
                2: "Alaska",
                4: "Arizona",
                5: "Arkansas",
                6: "California",
                8: "Colorado",
                9: "Connecticut",
                10: "Delaware",
                11: "Washington DC",
                12: "Florida",
                13: "Georgia",
                15: "Hawaii",
                16: "Idaho",
                17: "Illinois",
                18: "Indiana",
                19: "Iowa",
                20: "Kansas",
                21: "Kentucky",
                22: "Louisiana",
                23: "Maine",
                24: "Maryland",
                25: "Massachusetts",
                26: "Michigan",
                27: "Minnesota",
                28: "Mississippi",
                29: "Missouri",
                30: "Montana",
                31: "Nebraska",
                32: "Nevada",
                33: "New Hampshire",
                34: "New Jersey",
                35: "New Mexico",
                36: "New York",
                37: "North Carolina",
                38: "North Dakota",
                39: "Ohio",
                40: "Oklahoma",
                41: "Oregon",
                42: "Pennsylvania",
                44: "Rhode Island",
                45: "South Carolina",
                46: "South Dakota",
                47: "Tennessee",
                48: "Texas",
                49: "Utah",
                50: "Vermont",
                51: "Virginia",
                53: "Washington",
                54: "West Virginia",
                55: "Wisconsin",
                56: "Wyoming"
            }
        },
        "V201646": {
            "column": "PRE_PartyMoreHouseMembers",
            "labels": {
                1: "correct (D)",
                2: "incorrect (R)"
            }
        },
        "V201645": {
            "column": "PRE_FederalSpendingKnowledge",
            "labels": {
                1: "correct (Foreign aid)",
                0: "incorrect (Medicare, National defense, SS)"
            }
        },
        "V201380": {
            "column": "PRE_CorruptionView",
            "labels": {
                1: "Increased",
                2: "Decreased",
                3: "Stayed the same"
            }
        },
        "V202051": {
            "column": "POST_RegistrationStatus",
            "labels": {
                1: "Registered at this address",
                2: "Registered at a different address",
                3: "Not currently registered"
            }
        },
        "V202068x": {
            "column": "POST_Voted2020",
            "labels": {
                0: "Not registered and did not vote",
                1: "Registered and did not vote",
                2: "Voted"
            }
        },
        "V202073": {
            "column": "POST_VotePresident",
            "labels": {
                1: "Joe Biden",
                2: "Donald Trump",
                3: "Jo Jorgensen",
                4: "Howie Hawkins",
                5: "Other candidate {SPECIFY}"
            }
        },
        "V202205y1": {
            "column": "POST_ProblemMention",
            "labels": {
                1: "Defense spending",
                2: "Middle East",
                3: "Iraq",
                4: "War",
                5: "Terrorism",
                6: "Veterans",
                7: "National defense (all other)",
                8: "Foreign aid",
                9: "Foreign Trade",
                10: "Protection of US jobs",
                11: "Serbia /Balkans",
                12: "China",
                13: "International affairs (all other)",
                14: "Energy crisis",
                15: "Energy prices",
                16: "Energy (all other)",
                17: "Environment",
                18: "Natural Resources (all other)",
                19: "Education and training",
                20: "School funding",
                21: "Education (all other)",
                22: "AIDS",
                23: "Medicare",
                24: "Health (all other)",
                25: "Welfare",
                26: "Poverty",
                27: "Employment",
                28: "Housing",
                29: "Social security",
                30: "Income (all other)",
                31: "Crime",
                32: "Race relations",
                33: "Illegal drugs",
                34: "Police problems",
                35: "Guns",
                36: "Corporate Corruption",
                37: "Justice (all other)",
                38: "Budget",
                39: "Size of government",
                40: "Taxes",
                41: "Immigration",
                42: "Campaign finance",
                43: "Political corruption",
                44: "Ethics",
                45: "Government power",
                46: "Budget priorities",
                47: "Partisan politics",
                48: "Politicians",
                49: "Government (all other)",
                50: "The economy",
                51: "Stock market",
                52: "Economic inequality",
                53: "Recession",
                54: "Inflation",
                55: "Economics (all other)",
                56: "Agriculture",
                57: "Science",
                58: "Commerce",
                59: "Transportation",
                60: "Community development",
                61: "Abortion",
                62: "Child care",
                63: "Overpopulation",
                64: "Public morality",
                65: "Domestic violence",
                66: "Family",
                67: "Young people",
                68: "Sexual identity /LGBT+ issues",
                69: "The media",
                75: "Sexism /Gender issues",
                76: "Afghanistan",
                77: "Syria",
                78: "Elections",
                79: "Religion",
                80: "Civility",
                81: "Unity /division",
                82: "Health care",
                83: "Other"
            }
        }
    }
    return column_labels