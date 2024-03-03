from pathlib import Path
import json
import multiprocessing



def fix_filename(file):
    with open(file) as f:
        data = json.load(f)
    if 'conservation_scores' not in data:
        return
    cons_filename = Path(data['conservation_scores']['aln_property_entropy']).name
    cons_score_folder = Path('./alignment_conservation_scores/aln_property_entropy/')
    outfile = cons_score_folder / cons_filename
    data['conservation_scores']['aln_property_entropy'] = str(outfile.resolve())
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)



def main():
    json_files = list(Path('./info_jsons/').rglob('*.json'))
    p = multiprocessing.Pool(8)
    p.map(fix_filename, json_files)
    p.close()
    p.join()


if __name__ == "__main__":
    main()
