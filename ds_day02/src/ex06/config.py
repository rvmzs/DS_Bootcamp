
num_of_steps = 3
telegram_bot_token = '7251670520:AAGbwtY3zrVsB156znye-sgF6A9oxti1sy0'
telegram_chat_id = '-4742945413'


report_template = """
Report
We have made {total_observations} observations from tossing a coin: {tails} of them were tails and {heads} of them were heads.
The probabilities are {tail_probability}% and {head_probability}%, respectively.
Our forecast is that in the next {num_of_steps} observations we will have: {forecast_tails} tails and {forecast_heads} heads.
"""
