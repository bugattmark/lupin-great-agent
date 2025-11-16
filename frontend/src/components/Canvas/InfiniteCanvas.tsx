import { TransformWrapper, TransformComponent } from 'react-zoom-pan-pinch';
import { CenterChatBox } from './CenterChatBox';
import { ExternalPanel } from './ExternalPanel';
import { CanvasControls } from './CanvasControls';
import './InfiniteCanvas.css';

export function InfiniteCanvas() {
  return (
    <div className="infinite-canvas-container">
      <TransformWrapper
        initialScale={1}
        minScale={0.5}
        maxScale={2}
        centerOnInit
        limitToBounds={false}
        panning={{ disabled: false }}
        wheel={{ step: 0.1 }}
      >
        {({ zoomIn, zoomOut, resetTransform }) => (
          <>
            <CanvasControls
              onZoomIn={zoomIn}
              onZoomOut={zoomOut}
              onReset={resetTransform}
            />
            <TransformComponent
              wrapperClass="transform-wrapper"
              contentClass="transform-content"
            >
              <div className="canvas-content">
                <div className="canvas-center">
                  <CenterChatBox />
                  <ExternalPanel />
                </div>
              </div>
            </TransformComponent>
          </>
        )}
      </TransformWrapper>
    </div>
  );
}
