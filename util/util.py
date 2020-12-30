import OpenGL.GL as GL11;
import math;

class Vec:
	def __init__(self, x, y, z):
		self.x, self.y, self.z = x, y, z;

	def length(self):
		return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z);

	def __str__(self):
		return "x = " + self.x + " y = " + self.y + " z = " + self.z;

class Rect:
	def __init__(self, x, y, w, h):
		self.x, self.y, self.w, self.h = x, y, w, h;

def lerp(a, b, ticks):
	return a + (b - a) * ticks;

def distance3v(v, vv):
	x = v.x - vv.x;
	y = v.y - vv.y;
	z = v.z - vv.z;

	return math.sqrt(x * x + y * y + z * z);

def distance2r(r, rr):
	x = r.x - rr.x;
	y = r.y - rr.y;

	return math.sqrt(x * x + y * y);

def color(r, g, b, a = 255):
	GL11.glColor(r / 255.0, g / 255.0, b / 255.0, a / 255.0);

def drawRect(rect):
	GL11.glPushMatrix();

	GL11.glEnable(GL11.GL_BLEND);
	GL11.glBlendFunc(GL11.GL_SRC_ALPHA, GL11.GL_ONE_MINUS_SRC_ALPHA);

	GL11.glBegin(GL11.GL_QUADS);
	
	GL11.glVertex(rect.x, rect.y);
	GL11.glVertex(rect.x, rect.y + rect.h);
	GL11.glVertex(rect.x + rect.w, rect.y + rect.h);
	GL11.glVertex(rect.x + rect.w, rect.y);
	
	GL11.glEnd();

	GL11.glDisable(GL11.GL_BLEND);
	GL11.glPopMatrix();