import pandas as pd
from django.core.management.base import BaseCommand
from firstapp.models import customer_order


class Command(BaseCommand):
    help = "Import customer orders from a CSV using pandas"

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file",
            type=str,
            help="Path to the CSV file",
        )

    def handle(self, *args, **options):
        csv_file = options["csv_file"]
        df = pd.read_csv(csv_file)

        created = 0
        skipped = 0

        # Get all existing IDs to avoid duplicates
        existing_ids = set(customer_order.objects.values_list("id", flat=True))

        for _, row in df.iterrows():
            order_id = int(row["id"])

            if order_id in existing_ids:
                skipped += 1
                self.stdout.write(
                    self.style.WARNING(f"Skipped duplicate ID: {order_id}")
                )
                continue

            customer_order.objects.create(
                id=order_id,
                customer_first_name=row["first_name"],
                customer_last_name=row["last_name"],
                shoe_type=row["shoe_type"],
                shoe_material=row["shoe_material"],
                shoe_color=row["shoe_color"],
                total_amount=row["price"],
                is_completed=row["repair"],  # Make sure your CSV column is True/False
            )

            existing_ids.add(order_id)
            created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Import complete ✅ Created: {created}, Skipped: {skipped}"
            )
        )
