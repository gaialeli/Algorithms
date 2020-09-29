

def merge_ranges(meetings):
    
    """
    Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day 
    when everyone is available.
    
    This function takes a list of multiple meeting time ranges and returns a list of condensed ranges.
    """
    
    # STEP 1: SORTING -- we sort the meetings by their start time
    sorted_meetings = sorted(meetings)
    
    # we create a list of merged mettings and we inizialized it with the first (meaning the earliest) meeting
    merged_meetings = [sorted_meetings[0]]
    
    for current_meeting_start, current_meeting_end in sorted_meetings[1:]: 
        
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]
        # If current meeting overlaps with last merged meeting then use the later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))
            
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings

my_meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

merged_meetings =  merge_ranges(my_meetings)


# expected outcome from the function: [(0, 1), (3, 8), (9, 12)]
