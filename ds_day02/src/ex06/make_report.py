import sys
from config import num_of_steps, report_template
from analytics import Research, Analytics

def main():
    try:
        research = Research()
        content = research.file_reader()

        calculations = Research.Calculations(content)
        head_count, tail_count = calculations.counts()
        head_percent, tail_percent = calculations.fractions(head_count, tail_count)

        analytics = Analytics(content)
        random_predictions = analytics.predict_random(num_of_steps)
        forecast_heads = sum(row[0] for row in random_predictions)
        forecast_tails = sum(row[1] for row in random_predictions)

        total_observations = len(content)

        report_data = report_template.format(
            total_observations=total_observations,
            tails=tail_count,
            heads=head_count,
            tail_probability=tail_percent,
            head_probability=head_percent,
            num_of_steps=num_of_steps,
            forecast_tails=forecast_tails,
            forecast_heads=forecast_heads
        )

        analytics.save_file(report_data, 'report', 'txt')
        research.send_telegram_message('The report has been successfully created')
    except Exception as e:
        research.send_telegram_message(f'The report hasn’t been created due to an error: {str(e)}')
        raise

if __name__ == '__main__':
    main()
