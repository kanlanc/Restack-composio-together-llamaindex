import { Card } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Search, Mail, Calendar, User } from "lucide-react";
import { Badge } from "@/components/ui/badge";

const EmailList = () => {
  return (
    <div className="space-y-6">
      <div className="relative">
        <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground h-4 w-4" />
        <Input placeholder="Search emails..." className="pl-10" />
      </div>

      <div className="grid gap-4">
        {[1, 2, 3].map((item) => (
          <Card
            key={item}
            className="p-4 hover:bg-accent/50 transition-colors cursor-pointer"
          >
            <div className="flex items-start gap-4">
              <div className="p-2 bg-secondary rounded-lg">
                <Mail className="h-6 w-6 text-foreground" />
              </div>
              <div className="flex-1">
                <div className="flex items-center justify-between mb-1">
                  <div className="flex items-center gap-2">
                    <h3 className="font-medium">
                      Re: Latest Newsletter Updates
                    </h3>
                    <Badge variant="secondary">Auto-reply</Badge>
                  </div>
                  <span className="text-sm text-muted-foreground flex items-center">
                    <Calendar className="h-4 w-4 mr-1" />2 days ago
                  </span>
                </div>
                <div className="flex items-center text-sm text-muted-foreground mb-2">
                  <User className="h-4 w-4 mr-1" />
                  <span>john.doe@example.com</span>
                </div>
                <p className="text-sm text-muted-foreground line-clamp-2">
                  Based on your interest in our latest newsletter, here are some
                  relevant articles that might help you...
                </p>
              </div>
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default EmailList;
