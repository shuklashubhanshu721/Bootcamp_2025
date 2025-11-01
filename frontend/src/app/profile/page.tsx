"use client";
import React, { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/context/AuthContext";
import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export default function ProfilePage() {
  const { token, logout } = useAuth();
  const router = useRouter();
  const [user, setUser] = useState<any>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!token) {
      router.push("/login");
      return;
    }

    const fetchUser = async () => {
      try {
        const res = await fetch("http://localhost:8000/api/v1/auth/users/me", {
          headers: { Authorization: `Bearer ${token}` },
        });
        if (res.status === 401) {
          logout();
          router.push("/login");
          return;
        }
        const data = await res.json();
        setUser(data);
      } catch (err) {
        setError("Failed to load profile info");
      }
    };

    fetchUser();
  }, [token, router, logout]);

  if (!token) return null;

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <Card className="p-8 w-full max-w-md space-y-4 text-center">
        <h1 className="text-2xl font-semibold">Profile</h1>
        {error && <p className="text-red-600">{error}</p>}
        {user ? (
          <>
            <p><strong>Email:</strong> {user.email}</p>
            <p><strong>Role:</strong> {user.role}</p>
            <p><strong>Status:</strong> {user.status}</p>
          </>
        ) : (
          <p>Loading user data...</p>
        )}
        <Button
          onClick={() => {
            logout();
            router.push("/login");
          }}
          className="w-full mt-4"
        >
          Logout
        </Button>
      </Card>
    </div>
  );
}