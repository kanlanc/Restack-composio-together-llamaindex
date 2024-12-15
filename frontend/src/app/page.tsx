"use client";

// import { useState } from "react";
import { toast } from "sonner";
import { Header } from "@/components/dashboard/Header";
import { DashboardTabs } from "@/components/dashboard/DashboardTabs";
import { Button } from "@/components/ui/button";

const Dashboard = () => {
  const handleCreateContentSource = () => {
    toast.info("Coming soon: Create new content source");
  };

  const handleConnectToGmail = () => {
    fetch("/api/gmail-auth", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        user_id: "saivicky2015@gmail.com", //FIXME: TODO: Lets assume you make the user login before they get to the dashboard page and so change this
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        window.location.href = data.redirect_url;
      });
  };

  return (
    <div className="min-h-screen bg-background max-w-7xl mx-auto p-8 my-8">
      <Header onCreateSource={handleCreateContentSource} />
      <DashboardTabs />
      <Button onClick={handleConnectToGmail} className="mt-4" variant="outline">
        <svg
          className="mr-2 h-4 w-4"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="currentColor"
        >
          <path d="M20.283 10.356h-8.327v3.451h4.792c-.446 2.193-2.313 3.453-4.792 3.453a5.27 5.27 0 0 1-5.279-5.28 5.27 5.27 0 0 1 5.279-5.279c1.259 0 2.397.447 3.29 1.178l2.6-2.599c-1.584-1.381-3.615-2.233-5.89-2.233a8.908 8.908 0 0 0-8.934 8.934 8.907 8.907 0 0 0 8.934 8.934c4.467 0 8.529-3.249 8.529-8.934 0-.528-.081-1.097-.202-1.625z" />
        </svg>
        Connect to Gmail
      </Button>
    </div>
  );
};

export default Dashboard;
