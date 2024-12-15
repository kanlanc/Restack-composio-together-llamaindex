import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Settings, Power } from "lucide-react";

interface ContentSourceCardProps {
  name: string;
  description: string;
  status: "active" | "inactive";
}

const ContentSourceCard = ({
  name,
  description,
  status,
}: ContentSourceCardProps) => {
  return (
    <Card className="p-6 card-hover">
      <div className="flex justify-between items-start mb-4">
        <div>
          <h3 className="font-semibold text-lg">{name}</h3>
          <p className="text-sm text-muted-foreground">{description}</p>
        </div>
        <Badge
          variant={status === "active" ? "default" : "secondary"}
          className="capitalize"
        >
          {status}
        </Badge>
      </div>

      <div className="flex justify-between items-center mt-6">
        <button className="text-sm text-muted-foreground hover:text-foreground transition-colors flex items-center">
          <Settings className="w-4 h-4 mr-1" />
          Configure
        </button>
        <button className="text-sm text-muted-foreground hover:text-foreground transition-colors flex items-center">
          <Power className="w-4 h-4 mr-1" />
          {status === "active" ? "Deactivate" : "Activate"}
        </button>
      </div>
    </Card>
  );
};

export default ContentSourceCard;
