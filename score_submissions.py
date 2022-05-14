import argparse
import os

import numpy as np
import pandas as pd


def anonymise_name(name: str) -> str:
    return ''.join(c for c in name if c.isupper())


def score_submissions(path_to_submissions_file: str, path_to_match_results_file: str) -> pd.DataFrame:
    match_results = pd.read_csv(path_to_match_results_file)
    mirrored_match_results = pd.DataFrame(
        {
            'player1_name': match_results['player2_name'],
            'player2_name': match_results['player1_name'],
            'Gender': match_results['Gender'],
            'player1_win': match_results['player2_win'],
            'player2_win': match_results['player1_win']
        }
    )
    submissions = pd.read_excel(path_to_submissions_file, sheet_name=None, engine='openpyxl')

    scores = []
    for name, submission in submissions.items():
        if name.startswith('!'):
            # Ignore malformed submission for now
            continue
        df = pd.concat(
            [
                match_results.merge(submission, on=['player1_name', 'player2_name', 'Gender']),
                mirrored_match_results.merge(submission, on=['player1_name', 'player2_name', 'Gender'])
            ]
        )
        assert len(df) == len(match_results)
        # Handle probabilities of 0
        df.loc[df['p_player1_win'] == 0, 'p_player1_win'] = 1e-12
        df.loc[df['p_player2_win'] == 0, 'p_player2_win'] = 1e-12
       
        # Normalise probabilities
        df['p_player1_win'] = df['p_player1_win'] / df[['p_player1_win', 'p_player2_win']].sum(axis=1)
        df['p_player2_win'] = df['p_player2_win'] / df[['p_player1_win', 'p_player2_win']].sum(axis=1)
        
        score = -(np.log(df['p_player1_win']) * df['player1_win'] + np.log(df['p_player2_win']) * df['player2_win']).sum()
        
        scores.append({'submission': anonymise_name(name), 'score': score})

    scores = pd.DataFrame(scores).sort_values(['score'])
    return scores


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--submissions-file',required=True)
    parser.add_argument('--match-results-file', required=True)
    parser.add_argument('--output-file', required=True)

    args = parser.parse_args()

    results = score_submissions(args.submissions_file, args.match_results_file)
    results.to_csv(args.output_file, index=False)


if __name__ == '__main__':
    main()

