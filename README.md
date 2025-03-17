# HarmoniCode

**HarmoniCode** is an Algorithmic Music Composer that generates original music compositions using code! This tool blends music theory with programming to create melodies and chord progressions, exportable as MIDI files for use in your favorite digital audio workstation (DAW). Whether you're a coder, musician, or both, HarmoniCode offers a playground for creativity at the intersection of technology and sound.

## Features
- **Melody Generation**: Creates random melodies based on a user-defined key, with a rhythmic motif for structure.
- **Chord Progressions**: Builds simple I-IV-V-I progressions with occasional inversions for variety.
- **User Customization**: Specify the key (e.g., C, G, F#) and tempo (BPM) interactively.
- **MIDI Export**: Outputs compositions as MIDI files, compatible with DAWs like Ableton Live, FL Studio, or GarageBand.
- **Extensible Design**: Built with Python and `music21`, ready for enhancements like additional instruments or machine learning integration.

## Why It’s Cool
HarmoniCode explores the fusion of algorithmic logic and musical creativity. Every run produces a unique piece, making it a limitless source of inspiration for musicians and a fun challenge for developers.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/frangedev/harmonicode.git
   cd harmonicode
   ```
2. **Install Dependencies**:
   Ensure you have Python 3.x installed, then run:
   ```bash
   pip install music21
   ```
3. **Run the Program**:
   ```bash
   python harmonicode.py
   ```

## Usage
1. Launch the script:
   ```bash
   python harmonicode.py
   ```
2. Follow the prompts:
   - Enter a key (e.g., `C`, `G`, `F#`) or press Enter for default (C Major).
   - Enter a tempo (e.g., `120`) or press Enter for default (120 BPM).
3. Check the output:
   - A MIDI file named `harmonicode_composition.mid` will be saved in the project directory.
   - Import it into your DAW to listen or edit!

## Example Output
- **Key**: C Major
- **Tempo**: 120 BPM
- **Melody**: 16 notes with a quarter-eighth-eighth motif.
- **Chords**: 8 measures of I-IV-V-I progression with inversions.

Open `harmonicode_composition.mid` in a MIDI editor to hear your unique creation!

## Requirements
- Python 3.x
- `music21` library (`pip install music21`)
- Optional: A MIDI player or DAW to listen to the output.

## Contributing
We’d love your help to make HarmoniCode even better! Here’s how to contribute:
1. Fork the repo.
2. Create a new branch (`git checkout -b feature/your-idea`).
3. Make your changes and commit (`git commit -m "Add cool feature"`).
4. Push to your fork (`git push origin feature/your-idea`).
5. Open a Pull Request.

Ideas for enhancements:
- Add support for minor scales or other modes.
- Integrate machine learning with Magenta for smarter compositions.
- Create a GUI for easier interaction.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built with [music21](http://web.mit.edu/music21/), a powerful toolkit for computer-aided musicology.
- Inspired by the endless possibilities of algorithmic art.
