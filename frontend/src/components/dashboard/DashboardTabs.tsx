import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { Database, Mail, BarChart } from "lucide-react";
import { ContentSourcesTab } from "./ContentSourcesTab";
import EmailListComponent from "@/components/EmailListComponent";
import AnalyticsComponent from "@/components/AnalyticsComponent";

export const DashboardTabs = () => (
  <main className="max-w-7xl mx-auto fade-in">
    <Tabs defaultValue="sources" className="space-y-6">
      <TabsList className="grid w-full grid-cols-3 lg:w-[400px]">
        <TabsTrigger value="sources" className="flex items-center gap-2">
          <Database className="h-4 w-4" />
          Content Sources
        </TabsTrigger>
        <TabsTrigger value="emails" className="flex items-center gap-2">
          <Mail className="h-4 w-4" />
          Email Replies
        </TabsTrigger>
        <TabsTrigger value="analytics" className="flex items-center gap-2">
          <BarChart className="h-4 w-4" />
          Analytics
        </TabsTrigger>
      </TabsList>

      <TabsContent value="sources" className="space-y-6">
        <ContentSourcesTab />
      </TabsContent>

      <TabsContent value="emails">
        <EmailListComponent />
      </TabsContent>

      <TabsContent value="analytics">
        <AnalyticsComponent />
      </TabsContent>
    </Tabs>
  </main>
);
