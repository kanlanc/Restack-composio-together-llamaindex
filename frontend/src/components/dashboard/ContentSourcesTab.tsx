import { Card } from "@/components/ui/card";
import { PlusCircle } from "lucide-react";
import ContentSourceCard from "@/components/dashboard/ContentSourceCard";

export const ContentSourcesTab = () => (
  <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
    <ContentSourceCard
      name="Blog Posts"
      description="Content from your blog posts"
      status="active"
    />
    <ContentSourceCard
      name="Newsletter Archive"
      description="Content from past newsletters"
      status="inactive"
    />
    <Card className="p-6 border-dashed border-2 flex items-center justify-center cursor-pointer hover:bg-accent/50 transition-colors">
      <div className="text-center text-muted-foreground">
        <PlusCircle className="w-8 h-8 mx-auto mb-2" />
        <p className="font-medium">Add New Source</p>
      </div>
    </Card>
  </div>
);
