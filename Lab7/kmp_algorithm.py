
def kmp_algorithm(string, substring):
    def prefix_function(substring):
        prefix_function_res = [0] * len(substring)
        for curr_substring_idx in range(1, len(substring)):
            curr_prefix_idx = prefix_function_res[curr_substring_idx - 1]
            while curr_prefix_idx > 0 and substring[curr_prefix_idx] != substring[curr_substring_idx]:
                curr_prefix_idx = prefix_function_res[curr_prefix_idx - 1]
            if substring[curr_prefix_idx] == substring[curr_substring_idx]:
                curr_prefix_idx += 1
            prefix_function_res[curr_substring_idx] = curr_prefix_idx
        return prefix_function_res

    prefix_function_res = prefix_function(substring)
    curr_substring_idx = 0
    kmp_res = []

    for curr_string_idx in range(len(string)):
        while curr_substring_idx > 0 and string[curr_string_idx] != substring[curr_substring_idx]:
            curr_substring_idx = prefix_function_res[curr_substring_idx - 1]
        if string[curr_string_idx] == substring[curr_substring_idx]:
            curr_substring_idx = curr_substring_idx + 1
        if curr_substring_idx == len(substring):
            kmp_res.append(curr_string_idx - curr_substring_idx + 1)
            curr_substring_idx = prefix_function_res[curr_substring_idx - 1]

    return kmp_res


test_string = "ABABABCABABACBCABABABC"
test_substring = "ABABAC"
print(kmp_algorithm(test_string, test_substring))
