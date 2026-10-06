import argparse
from scenarios.runner import run_scenario

def main():
    parser = argparse.ArgumentParser(description="Run a room temperature scenario")
    parser.add_argument("--scenario", required=True, help="Path to YAML scenario file")
    parser.add_argument("--runs", type=int, default=1, help="Number of Monte Carlo trials")
    args = parser.parse_args()
    run_scenario(args.scenario, runs=args.runs)

if __name__ == "__main__":
    main()
