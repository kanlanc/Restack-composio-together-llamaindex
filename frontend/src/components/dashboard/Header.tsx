import { Button } from "@/components/ui/button";
import { PlusCircle } from "lucide-react";

interface HeaderProps {
  onCreateSource: () => void;
}

export const Header = ({ onCreateSource }: HeaderProps) => (
  <header className="mb-8 fade-up">
    <div className="flex items-center justify-between mb-6">
      <div>
        <h1 className="text-4xl font-bold tracking-tight">CraftConnect</h1>
        <p className="text-muted-foreground mt-2">
          Manage your content sources and automated responses
        </p>
      </div>
      <Button onClick={onCreateSource} className="scale-in">
        <PlusCircle className="mr-2 h-4 w-4" />
        Create Content Source
      </Button>
    </div>
  </header>
);
