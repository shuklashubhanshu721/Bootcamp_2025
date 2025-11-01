"use client";

import React, { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Input } from "@/components/ui/input";

export default function QueryPage() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [citations, setCitations] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleAsk = async () => {
    if (!question.trim()) {
      setError("Please enter a question before submitting.");
      return;
    }
    setError("");
    setLoading(true);
    setAnswer("");
    setCitations([]);

    try {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000"}/api/v1/query/ask`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ question }),
        }
      );

      if (!response.ok) {
        const err = await response.json();
        throw new Error(err.detail || "Failed to fetch response");
      }

      const data = await response.json();
      setAnswer(data.answer || "No answer returned");
      if (data.citations) setCitations(data.citations);
    } catch (err: any) {
      setError(err.message || "An unexpected error occurred");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-gray-50 p-6">
      <Card className="p-6 w-full max-w-2xl shadow-lg">
        <h2 className="text-2xl font-semibold mb-4">Ask the Knowledge Base</h2>
        <Input
          type="text"
          placeholder="Type your question here..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          className="mb-4"
        />
        <Button onClick={handleAsk} disabled={loading} className="w-full">
          {loading ? "Thinking..." : "Ask"}
        </Button>
        {error && <p className="mt-4 text-red-600">{error}</p>}
        {answer && (
          <div className="mt-6 bg-white rounded p-4 shadow-sm">
            <h3 className="font-medium text-gray-800 mb-2">Answer:</h3>
            <p className="text-gray-700 whitespace-pre-line">{answer}</p>
          </div>
        )}
        {citations.length > 0 && (
          <div className="mt-4 bg-white rounded p-4 shadow-sm">
            <h4 className="font-medium text-gray-800 mb-2">Citations:</h4>
            <ul className="list-disc pl-6">
              {citations.map((cite, idx) => (
                <li key={idx} className="text-gray-600">{cite}</li>
              ))}
            </ul>
          </div>
        )}
      </Card>
    </main>
  );
}