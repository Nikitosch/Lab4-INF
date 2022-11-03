import main
import with_regex
import xml_to_yaml_libs
import xml_to_yaml_lib2
import time
competitors = (main,with_regex,xml_to_yaml_libs,xml_to_yaml_lib2)
best_result = 100000
winner = "me"
for competitor in competitors:
    start = time.time()
    for i in range(100):
        competitor.main()
    result = time.time() - start
    print(result)
    if result < best_result:
        winner, best_result = competitor, result
print(best_result, winner)
