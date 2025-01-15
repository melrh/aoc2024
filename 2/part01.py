reports = []

def safety(input):
    safe = True
    safeReports = 0

    for line in input.readlines():
        reports.append(line)

    for i in reports:

        report = list(map(int, i.split()))

        for j in range(1, len(report)):

            # Check if ascending or descending
            if report == sorted(report, reverse=True) or report == sorted(report):
                safe = True
            else:
                safe = False
                break
            
            diff = (report[j] - report[j - 1])

            # Check that difference between number is >= 1 and <= 3
            if diff >= 1 and diff <= 3 and diff != 0:
                safe = True
            elif diff <= -1 and diff >= -3 and diff != 0:
                safe = True
            else:
                safe = False
                break

        if safe:
            safeReports += 1

    return safeReports


if __name__ == "__main__":
    with open('./input') as file:
        print("Safe Reports: " + str(safety(file)))