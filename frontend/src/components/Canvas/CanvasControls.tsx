import './CanvasControls.css';

interface CanvasControlsProps {
  onZoomIn: () => void;
  onZoomOut: () => void;
  onReset: () => void;
}

export function CanvasControls({ onZoomIn, onZoomOut, onReset }: CanvasControlsProps) {
  return (
    <div className="canvas-controls">
      <button onClick={onZoomIn} className="control-btn" title="Zoom In">
        +
      </button>
      <button onClick={onZoomOut} className="control-btn" title="Zoom Out">
        −
      </button>
      <button onClick={onReset} className="control-btn" title="Reset View">
        ⟲
      </button>
    </div>
  );
}
