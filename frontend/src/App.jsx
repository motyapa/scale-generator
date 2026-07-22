import {useEffect, useRef, useState} from 'react'
import './App.css'
import {OpenSheetMusicDisplay} from "opensheetmusicdisplay";

function App() {
  const majorKeys = ["Ab", "A", "Bb", "B", "Cb", "C", "C#", "Db", "D", "Eb", "E", "F", "F#", "Gb", "G"];
  const minorKeys = ["Ab", "A", "A#", "Bb", "B", "C", "C#", "D", "D#", "Eb", "E", "F", "F#", "G", "G#"];

  const containerRef = useRef(null)

  const [mode, setKeys] = useState("Major");
  const keys = mode === "Major" ? majorKeys : minorKeys;

  const [config, setConfig] = useState({
    exerciseType: "Rows",
    exerciseSize: 2,
    modeType: "Major",
    includeNoteNames: true,
    key: "C",
    rhythm: "Quarter",
    octaveOne: 3,
    octaveTwo: 4
  });

  const osmdRef = useRef(null)
  useEffect(() => {
    const osmdRef = new OpenSheetMusicDisplay(containerRef.current, {
      autoResize: true,
    });
  }, []);

  async function generateExercise(config) {
    const response = await fetch(
      "http://localhost:8000/generate-exercise",
      {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
          type: config.exerciseType,
          mode: config.modeType,
          include_note_as_lyric: config.includeNoteNames,
          key: config.key,
          exercise_size: config.exerciseSize,
          rhythm: config.rhythm,
          octave_one: config.octaveOne,
          octave_two: config.octaveTwo
        }),
      },
    )

    const xml = await response.text()
    await osmdRef.current.load(xml)
    osmdRef.current.render()
  }

  return (
    <>
      <section id="center">
        <div className="settings-grid">
          <div className="form-row">
            <label>Exercise Type:</label>
            <select value={config.exerciseType} onChange={(e) => setConfig({...config, exerciseType: e.target.value})}>
              <option value="Rows">Rows</option>
              <option value="Skips">Skips</option>
              <option value="Intervals">Intervals</option>
            </select>
          </div>
          <div className='form-row'>
            <label>Size of {config.exerciseType}: </label>
            <input type="number" value={config.exerciseSize} onChange={(e) => setConfig({...config, exerciseSize: e.target.valueAsNumber})}></input>
          </div>
          <div className="form-row">
            <label>Key: </label>
            <select value={config.key} onChange={(e) => setConfig({...config, key: e.target.value})}>
              {keys.map((key) => (<option key={key} value={key}>{key}</option>))}
            </select>
          </div>
          <div className='form-row'>
            <label>Mode: </label>
            <select
              value={config.modeType}
              onChange={(e) => {
                const newMode = e.target.value;
                setKeys(newMode);
                setConfig({
                  ...config,
                  modeType: newMode,
                  key: newMode === "Major" ? (majorKeys.includes(config.key) ? config.key : "C") : (minorKeys.includes(config.key) ? config.key : "A")
                })
              }}
          >
              <option value="Major">Major</option>
              <option value="Minor">Minor</option>
            </select>
          </div>
          <div className="form-row">
            <label>Rhythm: </label>
            <select value={config.rhythm} onChange={(e) => setConfig({...config, rhythm: e.target.value})}>
              <option value="Whole">Whole Notes</option>
              <option value="Half">Half Notes</option>
              <option value="Quarter">Quarter Notes</option>
              <option value="Eighth">Eighth Notes</option>
              <option value="Sixteenth">Sixteenth Notes</option>
              <option value="Triplet">Triplets</option>
            </select>
          </div>
          <div className='form-row'>
            <label>Include note names? </label>
            <select value={config.includeNoteNames} onChange={(e) => setConfig({...config, includeNoteNames: e.target.value === 'true'})}>
              <option value="true">Include note names</option>
              <option value="false">Do not include note names</option>
            </select>
          </div>
          <div className='form-row'>
            <label>Octave Range: <span title="If high to low, it will create a descending exercise, otherwise it will create an ascending exercise">ⓘ</span></label>
            <input type="number" value={config.octaveOne} onChange={(e) => setConfig({...config, octaveOne: e.target.valueAsNumber})}></input>
          </div>
          <div className='form-row'>
            <label> to </label>
            <input type="number" value={config.octaveTwo} onChange={(e) => setConfig({...config, octaveTwo: e.target.valueAsNumber})}></input>
          </div>
        </div>
        <button
          type="button"
          className="counter"
          onClick={() => generateExercise(config)}
        >
          Generate Exercise
        </button>
      </section>
      <div style={{ display: "flex", justifyContent: "center" }}>
        <div style={{width: "80%"}} ref={containerRef} />
      </div>
    </>
  )
}

export default App
