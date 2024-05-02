# # A =  final amount
# # P =  initial principal balance
# # r =  annual interest rate
# # t =  time (in years)
# # A = P (1 + rt)

# import sys


# def simple_interest(principle_amount, interest_rate, time_in_months):
#     """
#     :param principle_amount:
#     :param interest_rate:
#     :param time_in_months:
#     :return:
#     """
#     total_amount = principle_amount * (1 + interest_rate * time_in_months / 100)
#     return total_amount

# # import ipdb;ipdb.set_trace()
# # print(sys.argv)
# principle_amount = float(sys.argv[1])
# interest_rate = float(sys.argv[2])
# time_in_months = float(sys.argv[3])

# amount = simple_interest(principle_amount, interest_rate, time_in_months)
# print("Total amount: ", amount) 