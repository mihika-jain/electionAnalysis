import sys
def dict_time_series():
    dict_time_series = {
      "VCF0888": {"column":"DecCrimeFedSpending", "unique_values": 3, "type":"rank", "2020":"V201309"},
      "VCF0310" : {"column":"interestInElection", "unique_values": 3, "type":"rank", "2020": "V201006"},
      "VCF0879" : {"column": "DecIllegalAliens", "unique_values": 5, "type": "rank", "2020": "V202232"},
      "VCF0713" : {"column": "PRE_IntentVote", "unique_values": 4, "type": "cat", "2020": "V201033"},
      "VCF0004": {"column": "Year", "unique_values": sys.maxsize, "type": "num"},
      "VCF0104": {"column": "Sex", "unique_values": 2, "type": "cat", "2020": "V201600"},
      "VCF0301": {"column": "PartyIDRepublican", "unique_values": 7, "type": "rank", "2020": "V201231x"},
      "VCF0839": {"column": "IncSpendingServices", "unique_values": 7, "type": "rank", "2020": "V201246"},
      "VCF0130" : {"column": "WeakReligiousAttendence", "unique_values":5, "type":"rank", "2020": "V201453"},
      #"VCF0650": {"column": "FedGovPerformance", "unique_values": 8, "type": "rank"},
      #"VCF0656": {"column": "GovTrust", "unique_values": 100, "type": "rank"},
      #"VCF0730": {"column": "PartyMoreHouseMembers", "unique_values": 2, "type": "cat"},    
      "VCF0871": {"column": "WorseEconomyView", "unique_values": 5, "type": "rank", "2020":"V201327x"},
      "VCF0838": {"column": "AbortionRightsSC", "unique_values": 4, "type": "cat", "2020": "V201336"},
      "VCF0101": {"column": "Age", "unique_values": 96, "type": "num", "2020": "V201507x"},
      "VCF0110": {"column": "EducationLevel", "unique_values": 4, "type": "cat", "2020": "V201511x"},
      "VCF0114": {"column": "Income", "unique_values": 5, "type": "cat", "2020": "V202468x"},
      "VCF0105a": {"column": "Race", "unique_values": 6, "type": "cat", "2020": "V201549x" },
      "VCF0112": {"column": "Region", "unique_values": 4, "type": "cat", "2020": "V203003" },
      #"VCF0138": {"column": "HouseholdChildren", "unique_values": 4, "type": "rank"},
      "VCF0843": {"column": "IncDefenseSpending", "unique_values": 7, "type": "rank", "2020": "V201249"},
      "VCF0806": {"column": "IncPrivateMedInsurance", "unique_values": 7, "type": "rank", "2020": "V201252"},
      #"VCF0834" : {"column": "WomenRights", "unique_values": 7, "type": "rank"},
      "VCF0703": {"column": "RegistrationStatus", "unique_values": 2, "type": "cat", "2020": "V202068x"},
      "VCF0702": {"column": "Voted", "unique_values": 2, "type": "cat", "2020": "V202109x"},
      "VCF0704a": {"column": "VotePresident", "unique_values": 2, "type": "cat", "2020": "V202110x" },
      #"VCF0615": {"column": "VoteMatter", "unique_values": 2, "type": "cat"},
      "VCF0127" : {"column": "HH_In_Union", "unique_values": 2, "type": "cat", "2020":"V201544" },
      "VCF0147" : {"column": "MaritalStatus", "unique_values": 7, "type": "cat", "2020":"V201508"},
      "VCF0606" : {"column": "FedTaxesNotWasted", "unique_values": 3, "type": "rank", "2020": "V201235"},
      "VCF9238"  : {"column": "EasierBuyGun", "unique_values": 3, "type": "rank", "2020": "V202337"},
      "VCF0853": {"column": "DecEmphasisOnTraditionalValues", "unique_values": 5, "type": "rank", "2020":"V202265"},
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


def rewrite_dict_replace_2020(data_dict):
    """
    Rewrites the given dictionary by replacing the original keys with the "2020" field's value.
    Removes the "2020" field from the dictionary.

    Args:
        data_dict (dict): Original dictionary with 2020 data fields.

    Returns:
        dict: Updated dictionary with modified keys and no "2020" fields.
    """
    updated_dict = {}

    for key, value in data_dict.items():
        if "2020" in value:
            new_key = value.pop("2020")  # Use the 2020 field's value as the new key
            updated_dict[new_key] = value  # Add the updated entry

    return updated_dict

def rewrite_column_labels_time(column_labels_time, dict_time_series):
    # Create a new dictionary to store the updated column labels
    updated_column_labels_time = {}

    # Iterate over each entry in the column_labels_time dictionary
    for key, value in column_labels_time.items():
        # Extract the "2020" value from the dict_time_series for the corresponding key
        if key in dict_time_series and key in column_labels_time:
            # Use the value in the "2020" field from dict_time_series to update the key
            #print(dict_time_series[key]['column'])
            new_key = dict_time_series[key]["2020"]
            #print(value)
        
            # Add the updated key and the associated value (column and labels) to the new dictionary
            updated_column_labels_time[new_key] = value

    return updated_column_labels_time
