import { useState } from 'react';
import './ExternalPanel.css';

interface Attempt {
  model: string;
  prompt: string;
  response: string;
  success: boolean;
  timestamp: Date;
}

export function ExternalPanel() {
  const [isOpen, setIsOpen] = useState(true);
  const [attempts, setAttempts] = useState<Attempt[]>([]);
  const [activeTab, setActiveTab] = useState<'attempts' | 'conversation'>('attempts');

  return (
    <div className={`external-panel ${isOpen ? 'open' : 'closed'}`}>
      <div className="panel-header">
        <h3>EXTERNAL LLM</h3>
        <button
          className="toggle-btn"
          onClick={() => setIsOpen(!isOpen)}
        >
          {isOpen ? '→' : '←'}
        </button>
      </div>

      {isOpen && (
        <>
          <div className="panel-tabs">
            <button
              className={`tab ${activeTab === 'attempts' ? 'active' : ''}`}
              onClick={() => setActiveTab('attempts')}
            >
              Jailbreak Attempts
            </button>
            <button
              className={`tab ${activeTab === 'conversation' ? 'active' : ''}`}
              onClick={() => setActiveTab('conversation')}
            >
              Conversation
            </button>
          </div>

          <div className="panel-content">
            {activeTab === 'attempts' && (
              <div className="attempts-list">
                {attempts.length === 0 ? (
                  <div className="empty-state">
                    No jailbreak attempts yet
                  </div>
                ) : (
                  attempts.map((attempt, idx) => (
                    <div key={idx} className={`attempt ${attempt.success ? 'success' : 'failed'}`}>
                      <div className="attempt-header">
                        <span className="attempt-model">{attempt.model}</span>
                        <span className={`attempt-status ${attempt.success ? 'success' : 'failed'}`}>
                          {attempt.success ? '✓' : '✗'}
                        </span>
                      </div>
                      <div className="attempt-prompt">{attempt.prompt}</div>
                      <div className="attempt-response">{attempt.response}</div>
                    </div>
                  ))
                )}
              </div>
            )}

            {activeTab === 'conversation' && (
              <div className="conversation-view">
                <div className="empty-state">
                  No active conversation
                </div>
              </div>
            )}
          </div>
        </>
      )}
    </div>
  );
}
