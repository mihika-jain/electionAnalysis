import sys
def dict_time_series():
    dict_time_series = {
      "VCF0888": {"column":"incCrimeFedSpending", "unique_values": 3, "type":"rank"},
      "VCF0310" : {"column":"interestInElection", "unique_values": 3, "type":"rank"},
      "VCF0879" : {"column": "illegalAliens", "unique_values": 5, "type": "rank"},
      "VCF0713" : {"column": "PRE_IntentVote", "unique_values": 4, "type": "cat"},
      "VCF0004": {"column": "Year", "unique_values": sys.maxsize, "type": "num"},
      "VCF0104": {"column": "Sex", "unique_values": 2, "type": "cat"},
      "VCF0301": {"column": "PartyID", "unique_values": 7, "type": "rank"},
      "VCF0839": {"column": "ScaleSpendingServices", "unique_values": 7, "type": "rank"},
      "VCF0130" : {"column": "religiousAttendence", "unique_values":5, "type":"rank"},
      "VCF0650": {"column": "FedGovPerformance", "unique_values": 8, "type": "rank"},
      "VCF0656": {"column": "GovTrust", "unique_values": 100, "type": "rank"},
      "VCF0730": {"column": "PartyMoreHouseMembers", "unique_values": 2, "type": "cat"},    
      "VCF0871": {"column": "EconomyView", "unique_values": 5, "type": "rank"},
      "VCF0838": {"column": "AbortionRightsSC", "unique_values": 4, "type": "cat"},
      "VCF0101": {"column": "Age", "unique_values": 96, "type": "num"},
      "VCF0110": {"column": "EducationLevel", "unique_values": 4, "type": "cat"},
      "VCF0114": {"column": "Income", "unique_values": 5, "type": "cat"},
      "VCF0105a": {"column": "Race", "unique_values": 6, "type": "cat"},
      "VCF0112": {"column": "Region", "unique_values": 4, "type": "cat"},
      "VCF0138": {"column": "HouseholdChildren", "unique_values": 4, "type": "rank"},
      "VCF0843": {"column": "ScaleDefenseSpending", "unique_values": 7, "type": "rank"},
      "VCF0806": {"column": "ScaleMedInsurance", "unique_values": 7, "type": "rank"},
      "VCF0834" : {"column": "WomenRights", "unique_values": 7, "type": "rank"},
      "VCF0703": {"column": "RegistrationStatus", "unique_values": 2, "type": "cat"},
      "VCF0702": {"column": "Voted", "unique_values": 2, "type": "cat"},
      "VCF0704a": {"column": "VotePresident", "unique_values": 2, "type": "cat"},
      "VCF0615": {"column": "VoteMatter", "unique_values": 2, "type": "cat"},
      "VCF0127" : {"column": "HH_In_Union", "unique_values": 2, "type": "cat"},
      "VCF0147" : {"column": "MaritalStatus", "unique_values": 7, "type": "cat"},
      "VCF0606" : {"column": "FedWasteTaxes", "unique_values": 3, "type": "rank"},
      "VCF9238"  : {"column": "EasierBuyGun", "unique_values": 3, "type": "rank"},
      "VCF0853": {"column": "TraditionalValues", "unique_values": 5, "type": "rank"},
    }
    return dict_time_series


def column_labels_time():
    column_labels_time = {
        "VCF0147" : {
            "column": "MaritalStatus",
            "labels": {
                1: "Married" ,
                2: "Never_married", 
                3: "Divorced" ,
                4: "Separated",
                5: "Widowed" ,
                7: "Partners",
            }
        },
        "VCF0127" : {
            "column": "HH_In_Union",
            "labels": {
                1: "Yes", 
                2: "No",
            }
        },
        "VCF0713": {
            "column": "PRE_IntentVote",
            "labels": {
                1: "Democratic", 
                2: "Republican",
                3: "Undecided",
                4: "not intend to vote"
            }
        },
        "VCF0615": {
            "column": "VoteMatter",
            "labels": {
                1: "Yes",
                2: "No"
            }
        },
        "VCF0104": {
            "column": "Sex",
            "labels": {
                1: "Male",
                2: "Female"
            }
        },
        "VCF0128a": {
            "column": "religion",
            "labels": {
                1: "Mainline Protestant",
                2: "Evangelical Protestant",
                3: "Catholic [Roman Catholic]",
                4: "Jewish",
                5: "Non-traditional orthodox",
                6: "Non-Christian/Non-Jewish",
                7: "Atheist, agnostic, none"
            }
        },
        "VCF0730": {
            "column": "PartyMoreHouseMembers",
            "labels": {
                1: "Incorrect party",
                2: "Correct party"
            }
        },
        "VCF0838": {
            "column": "AbortionRightsSC",
            "labels": {
                1: "never",
                2: "exception_rape_incest_saveLife",
                3: "exception_clearly_established",
                4: "choice"
            }
        },
        "VCF0110": {
            "column": "EducationLevel",
            "labels": {
                1: "Grade school",
                2: "High school",
                3: "Some college",
                4: "College"
            }
        },
        "VCF0114": {
            "column": "Income",
            "labels": {
                1: "0 to 16 percentile",
                2: "17 to 33 percentile",
                3: "34 to 67 percentile",
                4: "68 to 95 percentile",
                5: "96 to 100 percentile"
            }
        },
        "VCF0105a": {
            "column": "Race",
            "labels": {
                1: "White",
                2: "Black",
                3: "Asian_Pacific Islander",
                4: "American Indian_Alaska Native",
                5: "Hispanic",
                6: "Other"
            }
        },
        "VCF0112": {
            "column": "Region",
            "labels": {
                1: "Northeast",
                2: "North Central",
                3: "South",
                4: "West"
            }
        },
        "VCF0703": {
            "column": "RegistrationStatus",
            "labels": {
                1: "No",
                2: "Yes",
            }
        },
        "VCF0702": {
            "column": "Voted",
            "labels": {
                1: "No",
                2: "Yes"
            }
        },
        "VCF0704a": {
            "column": "VotePresident",
            "labels": {
                1: "Democrat",
                2: "Republican"
            }
        }
    }
    
    '''"VCF0302": {
        "column": "PartyID",
        "labels": {
            5: "Democratic party",
            1: "Republican party"
        }
    },'''

    return column_labels_time