"use client";

import { useEffect, useState } from "react";

export default function HealthPage() {
  const [status, setStatus] = useState("loading...");

  useEffect(() => {
    const checkHealth = async () => {
      try {
        const res = await fetch("http://127.0.0.1:8000/api/v1/health");
        const data = await res.json();
        setStatus(data.status || "unknown");
      } catch (err) {
        console.error("Health check failed:", err);
        setStatus("error");
      }
    };

    checkHealth();
  }, []);

  return (
    <main className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-2xl font-bold mb-4">System Health Check</h1>
      <p className="text-lg">Status: {status}</p>
    </main>
  );
}