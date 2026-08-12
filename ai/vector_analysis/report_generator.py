"""
=========================================================
Report Generator Module
=========================================================

Author  : Shivam Sahu
Project : AI Stock Market Intelligence System

Description
-----------
Generates a professional analysis report for the
Qdrant Vector Database.

Responsibilities
----------------
1. Vector Statistics Report
2. Payload Validation Report
3. Duplicate Detection Report
4. Overall Summary

=========================================================
"""


class ReportGenerator:

    LINE = "=" * 80
    SUB_LINE = "-" * 80

    # =====================================================
    # Heading
    # =====================================================

    @staticmethod
    def heading(title):

        print()
        print(ReportGenerator.LINE)
        print(title.center(80))
        print(ReportGenerator.LINE)

    # =====================================================
    # Section
    # =====================================================

    @staticmethod
    def section(title):

        print()
        print(title)
        print(ReportGenerator.SUB_LINE)

    # =====================================================
    # Dictionary Printer
    # =====================================================

    @staticmethod
    def print_dictionary(data):

        if not data:
            print("No Data Found")
            return

        for key, value in data.items():
            print(f"{str(key):35} {value}")

    # =====================================================
    # Statistics Report
    # =====================================================

    @staticmethod
    def statistics_report(stats):

        ReportGenerator.section("VECTOR STATISTICS")

        print(f"Total Vectors : {stats.total_vectors()}")

        # ----------------------------------------------

        ReportGenerator.section("SOURCE DISTRIBUTION")

        ReportGenerator.print_dictionary(
            stats.source_distribution()
        )

        # ----------------------------------------------

        ReportGenerator.section("TOPIC DISTRIBUTION")

        ReportGenerator.print_dictionary(
            stats.topic_distribution()
        )

        # ----------------------------------------------

        ReportGenerator.section("NEWS TYPE DISTRIBUTION")

        ReportGenerator.print_dictionary(
            stats.news_type_distribution()
        )

        # ----------------------------------------------

        ReportGenerator.section("SENTIMENT DISTRIBUTION")

        ReportGenerator.print_dictionary(
            stats.sentiment_distribution()
        )

        # ----------------------------------------------

        ReportGenerator.section("YEAR DISTRIBUTION")

        ReportGenerator.print_dictionary(
            stats.year_distribution()
        )

        # ----------------------------------------------

        ReportGenerator.section("DOCUMENT LENGTH")

        length = stats.document_length_distribution()

        print(f"Average Words   : {length['average_words']}")
        print(f"Median Words    : {length['median_words']}")
        print(f"Minimum Words   : {length['minimum_words']}")
        print(f"Maximum Words   : {length['maximum_words']}")
        print(f"Empty Documents : {length['empty_documents']}")

    # =====================================================
    # Payload Validation Report
    # =====================================================

    @staticmethod
    def payload_report(validator):

        ReportGenerator.section("PAYLOAD VALIDATION")

        report = validator.validate()

        for field, result in report.items():

            if field == "total_vectors":
                continue

            print(f"\n{field}")

            print(f"   Missing : {result['missing']}")
            print(f"   Empty   : {result['empty']}")
            print(f"   Valid   : {result['valid']}")

        # ----------------------------------------------

        ReportGenerator.section("PAYLOAD SUMMARY")

        summary = validator.summary()

        for key, value in summary.items():
            print(f"{key:35} {value}")

    # =====================================================
    # Duplicate Report
    # =====================================================

    @staticmethod
    def duplicate_report(detector):

        ReportGenerator.section("DUPLICATE DETECTION")

        summary = detector.summary()

        for key, value in summary.items():
            print(f"{key:35} {value}")

    # =====================================================
    # Final Report
    # =====================================================

    @staticmethod
    def final_summary(stats, validator, detector):

        ReportGenerator.heading(
            "QDRANT VECTOR DATABASE ANALYSIS REPORT"
        )

        ReportGenerator.statistics_report(stats)

        ReportGenerator.payload_report(validator)

        ReportGenerator.duplicate_report(detector)

        print()
        print(ReportGenerator.LINE)
        print("REPORT GENERATED SUCCESSFULLY".center(80))
        print(ReportGenerator.LINE)